import os
import torch

from diffusers import DiffusionPipeline
from accelerate import PartialState


def makedir(path):
    if not os.path.exists(path):
        os.mkdir(f"{path}")

def roundplus(x,y):
    if x%y==0:
        return x//y
    else:
        return (x//y)+1
    
def parallelizing_prompt(file_path, num_process):
    # Initialize an empty list to store the lists of 4 elements
    lists_of_prompts = []

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Iterate over the lines, creating lists of num_process elements
            for i in range(0, len(lines), num_process):
                # Extract num_process elements from the lines
                elements = [line.strip() for line in lines[i:i+num_process]]

                # Add the elements to the list_of_4_elements
                lists_of_prompts.append(elements)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lists_of_prompts


def main():
    height=728
    width=512
    docker_path = "/work/project"
    dir_name = "generated"
    prompt_file = "prompts.txt"
    guidance_scale = 5
    num_imgs = 20 
    multiple_gpus = True
    num_process = torch.cuda.device_count()
    negative_prompt = "nude, naked, fake, deformed iris, deformed pupils, bangs haircut, loose hair, profile picture, profile, three quarter view, 3d art, poor detail, Accessories, beard, dyed hair, colorful background, person of color, colored skin"
    if multiple_gpus:
        parallelized_negative_prompt = [negative_prompt]*num_process
    batch_size = 1
    model_card = "stablediffusionapi/realistic-vision-v51"
    
    with open(f'{docker_path}/{prompt_file}') as f:
        lines = f.readlines()

    if multiple_gpus: # num_process gpus
        list_of_prompts = parallelizing_prompt(prompt_file, num_process)
    else:
        prompts = []
        for i in lines:
            prompts.append(i.strip())

    pipe = DiffusionPipeline.from_pretrained(model_card, torch_dtype=torch.float16)

    if multiple_gpus:
        distributed_state = PartialState()
        pipe.to(distributed_state.device)
    else:
        pipe = pipe.to("cuda:0")

    num_imgs = roundplus(num_imgs,batch_size)

    makedir(f'{docker_path}/{dir_name}')


#########################################################
###################  Saving images   ####################
#########################################################    

    if multiple_gpus:
        inc=0
        for i, parallelized_prompt in enumerate(list_of_prompts):
            inc=0
            for j in range(num_imgs):
                with distributed_state.split_between_processes(parallelized_prompt) as prompt, distributed_state.split_between_processes(parallelized_negative_prompt) as negative_prompt:
                    images = pipe(prompt=prompt, negative_prompt=negative_prompt, guidance_scale=guidance_scale, height=height, width=width).images
                    for image in images:
                        image.save(f"{docker_path}/{dir_name}/{distributed_state.process_index}-{i}-{inc}.png")
                        inc+=1
    else:
        inc=0
        for i, prompt in enumerate(prompts):
            prompt = [prompt] * batch_size
            inc=0
            for j in range(num_imgs):
                images = pipe(prompt=prompt, negative_prompt=negative_prompt, height=height, width=width).images
                for image in images:
                    image.save(f"{docker_path}/{dir_name}/{i}-{inc}.png")
                    inc+=1



if __name__ == '__main__':
    main()