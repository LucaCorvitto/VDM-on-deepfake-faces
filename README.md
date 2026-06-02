# The more attractive the more real? Cognitive processes involved in deepfake detection in young and older adults
This repository contains the code and the process description of the generation of the synthetic photorealistic images used in the paper. The overview of all the info about the prompts and the model can be found in [info.xlsx](https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/info.xlsx).

## Abstract
Previous work had demonstrated the difficulty of humans to reliably distinguish between real and deepfake (i.e., created by artificial-intelligence) face stimuli. Given its important forensic implications including identity thefts, political misinformation, or fraud research in cognitive sciences has started to focus on face characteristics and cognitive mechanisms impacting deepfake detection accuracy. The perceived attractiveness of faces has been found to possibly facilitate deepfake detection (e.g., Miller et al., 2023). As particularly older adults are a vulnerable target group in the context of online frauds and misinformation susceptibility, the present study investigates, for the first time, whether subjectively perceived face attractiveness is associated with deepfake face detection in a sample of older (N = 37) and younger (N = 35) adults. Both groups of participants categorized 120 faces (50 % real, 50 % deepfake) as real or deepfake, followed by an attractiveness rating of each evaluated face. Both accuracy and response times were measured. Results confirm a lower detection accuracy in older adults. Moreover, perceived face attractiveness increased detection accuracy of real faces and decreased detection accuracy of deepfake faces, in both young and older adults. Finally, results on response times revealed that participants were slower to categorize real faces alongside increasingly attractive faces, suggesting the activation of more systematic decision making processes. These results provide the first preliminary insight into the cognitive processes, related to attractiveness and response times, involved in static deepfake face detection, in both young and older adults, and may provide a first step in the development of interventions and awareness campaigns tailored to different age groups.

## Images
The generated deepfakes dataset is available on [Huggingface](https://huggingface.co/datasets/LucaCorvitto/TheMoreAttractive_TheMoreReal). The dataset was created using the prompts inside the [`prompts.txt`](https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/prompts.txt) file. Each image's file name is structured in this way:
```
<#gpu>-<#prompt>-<#process>.png
```
where `<#gpu>` is the index of the gpu used for the image processing in a parallel gpu setup, `<#prompt>` is the associated index of the prompt in the [`prompts.txt`](prompts.txt) file, numbered from 0, and `<#process>` is the number representing the order in which the image was generated starting from 0 (seeds were not set or fixed). For example, the file named `0-0-0.png` is the 1-st generated image from the 1-st prompt in the prompts file by the gpu with index 0, while the one named `1-48-17.png` is the 18-th generated image from the 49-th prompt in the file by the gpu with index 1. 

After a first selection from the complete dataset, in order to standardize deepfake face stimuli making them comparable to real face stimuli, the images were manually edited in the following way: 
1. Removal of (grey) background
2. If applicable, removal of torso
3. If applicable, removal of visible pony-tails or braids (in case of tied-up hair of females)

Here follows a set of samples of the images generated and then manually edited for the study:

<table>
  <thead>
    <tr>
    <th>Name</th>
    <th>Prompt</th>
    <th>Generated Image</th>
    <th>Final Version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0-10-6</td>
      <td>ID photo for passport, a portrait photo of a white man with short hair, frontal view, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3, white background</td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-10-6.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-10-6-edited.png?raw=true" width="150"></td>
    </tr>
    <tr>
      <td>...<img width="100" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
      <td></td>
      <td><img width="200" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
      <td><img width="200" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
    </tr>
    <tr>
      <td>0-13-3</td>
      <td>ID photo for passport, a portrait photo of a white man with short black hair, frontal view, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3, white background</td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-13-3.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-13-3-edited.png?raw=true" width="150"></td>
    </tr>
    <tr>
      <td>...<img width="100" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
      <td></td>
      <td><img width="250" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
      <td><img width="250" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
    </tr>
    <tr>
      <td>0-23-2</td>
      <td>ID photo for passport, a portrait photo of an adult white woman with tied hair, frontal view, black eyes, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3, white background</td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-23-2.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-23-2-edited.png?raw=true" width="150"></td>
    </tr>
    <tr>
      <td>...<img width="100" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
      <td></td>
      <td><img width="250" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
      <td><img width="250" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"></td>
    </tr>
    <tr>
      <td>0-34-19</td>
      <td>ID photo for passport, a portrait photo of an adult white woman with tied hair, frontal view, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3, white background</td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-34-19.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/sample_images/0-34-19-edited.png?raw=true" width="150"></td>
    </tr>
  </tbody>
</table>

The final set of selected stimuli and other related information can be found on the official [OSF repo](https://osf.io/jnes3/overview?view_only=85e21df5286f4556ab228c9ed04ab59c).

## Prompts
The prompts slightly vary from each other in order to create diversified images, each one focused on a different detail, but the base is as follows:

**“ID photo for passport, a portrait photo of a white (wo)man, frontal view, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3, white background”**

The prompt is logically split in three main parts:
- The first one specifies the object of the request, so what is requested from the model to create
- The second one spcifies the subject of the image and its main  characteristics
- The last one is a list of descriptions that provides additional specifications for accurate image generation

The prompt is then further enhanced with additional descriptions to promote output variety:
- **With tied hair** / **with short hair**
- **Brown** / **black** / **blonde** / **ginger** (for hair color)
- **Brown** / **black eyes** (as I noticed a bias that led the model to generate many faces with blue eyes since "white" was specified as ethnicity)
- **Ponytail hair** / **without hair on forehead** (for female faces as generally tied hair alone was not enough to achieve the desired output)
- **Adult** (as the model had a bias towards generating images of young faces)

Follows an example of an enriched phrase (the complete list can be found [here](https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/prompts.txt)):

**"ID photo for passport, a portrait photo of an adult white woman with brown tied hair, frontal view, natural skin, 8k UHD, high quality, film grain, Fujifilm XT3, white background, ponytail hair"**

## Prompt Engineering
The first attempt was to use one of the prompts used in the paper ["On the use of Stable Diffusion for creating realistic faces: from generation to detection"](https://ieeexplore.ieee.org/abstract/document/10156981), which is as follows:

**"headshot portrait of a man with , real life, white monochromatic background, higly detailed, 50mm, HD, HDR color, 4k, studio lighting, Nikon, photography"**

Since the objective was to obtain images similar to the real samples, which had less natural light and more studio-like, with a completely white background, this prompt was not the most suitable, since instead it focuses on making the background and lights as natural as possible.

After several attempts, the best additions were:
- **ID photo for passport** (to make the model recreate images similar to those found in passports, with frontal faces and a white background)
- **Frontal view** (adding this specification allows the model to refer to images that adopt this shooting style, useful because ID passport did not always work)
- **White background** (which allowed for the creation of images with the most neutral background possible)
- **Ponytail hair** (for women, the addition of *frontal view* was necessary in combination with this modifier as most reference images were side-view photos focusing on the mane rather than the face)

## Negative Prompt
Another important aspect is the *negative prompt*. It is used in these models to give negative weights to characteristics that one wants to *avoid* appearing in the final image. This provides more control, specifically indicating what is wanted and what is not. The negative prompt used, also provided in [info.xlsx](https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/info.xlsx), is as follows:

**"nude, naked, fake, deformed iris, deformed pupils, bangs haircut, loose hair, profile picture, profile, three quarter view, 3d art, poor detail, Accessories, beard, dyed hair, colorful background, person of color, colored skin"**

Specifications are made to avoid all sort of artifacts that the model naturally tends to introduce, such as deformed pupils, rendered or poor detailed images, along as NSFW content, despite the filter already present in the model.

## Models
The models tested were [Stable diffusion v2](https://huggingface.co/Manojb/stable-diffusion-2-base), [dreamlike-art/dreamlike-photoreal-2.0](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0) and [stablediffusionapi/realistic-vision-v51](https://huggingface.co/stablediffusionapi/realistic-vision-v51), all based on [Stable Diffusion](https://arxiv.org/pdf/2112.10752).

The model used for the generation of the final images, the best performing one for this task, was Realistic Vision v5.1.
Specifically, the number of inference steps in the generation process and the width of the images were left to the default values, meanwhile:
- the **height** of the images was increased to obtain an aspect ratio similar to that used for ID/portrait half body photos
- the **guidance scale** was reduced to ensure a greater variation of faces, trying to keep it high enough to avoid the model ignoring important details specified in the prompt

The actual values are provided in [info.xlsx](https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/info.xlsx) and already set in the [script](https://github.com/LucaCorvitto/TheMoreAttractive_TheMoreReal/blob/main/main.py).
