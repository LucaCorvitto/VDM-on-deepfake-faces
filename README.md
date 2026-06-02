# Does the valence-dominance model apply to deepfake faces? Validation and its impact on deepfake detection
This repository contains the code and the process description of the generation of the synthetic photorealistic images used in the paper. The overview of all the info about the prompts and the model can be found in [info.xlsx](https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/info.xlsx).

## Abstract
Artificial Intelligence has given rise to increasingly more realistic fake contents such as deepfake faces, hardly distinguishable from real faces. However, evidence has shown that social evaluations of real faces are also able to impact the detection of deepfake faces. The present study aimed at applying for the first time the valence-dominance model for face evaluation on deepfake faces. Moreover, the impact of its thirteen attributes on deepfake detection performances was investigated. Specifically, 311 participants categorised 120 faces (50% real, 50% deepfake created ad hoc by Diffusion Model technology) and rated faces in regards to one of the attributes. Principal Component Analysis was applied in order to validate the valence-dominance model on deepfake faces, and a Brunwskian lens model was  applied to understand how each attribute contributes to a face being judged as deepfake. Results replicated the valence-dominance model on real faces as well as on faces categorized by participants as deepfake, but not on actual deepfake faces. Finally, the Brunwskian model revealed caringness and intelligence to impair detection of deepfake stimuli whilst weirdness was revealed to be a positive predictor, being positively associated with higher detection accuracy. Our results shed, for the first time, light into the differential cognitive processing of deepfake faces and their social evaluation whilst also providing novel insight into underlying mechanisms associated with deepfake detection. Interdisciplinary implications regarding the theoretical and applied contribution are discussed.

## Images
The generated deepfakes dataset is available on [HuggingFace](https://huggingface.co/datasets/LucaCorvitto/DeepFake-Faces-Stimuli). The dataset was created using the prompts inside the [`prompts.txt`](https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/prompts.txt) file. Each image's file name is structured in this way:
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
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-10-6.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-10-6-edited.png?raw=true" width="150"></td>
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
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-13-3.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-13-3-edited.png?raw=true" width="150"></td>
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
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-23-2.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-23-2-edited.png?raw=true" width="150"></td>
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
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-34-19.png?raw=true" width="150"></td>
      <td><img src="https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/sample_images/0-34-19-edited.png?raw=true" width="150"></td>
    </tr>
  </tbody>
</table>

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

Follows an example of an enriched phrase (the complete list can be found [here](https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/prompts.txt)):

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
Another important aspect is the *negative prompt*. It is used in these models to give negative weights to characteristics that one wants to *avoid* appearing in the final image. This provides more control, specifically indicating what is wanted and what is not. The negative prompt used, also provided in [info.xlsx](https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/info.xlsx), is as follows:

**"nude, naked, fake, deformed iris, deformed pupils, bangs haircut, loose hair, profile picture, profile, three quarter view, 3d art, poor detail, Accessories, beard, dyed hair, colorful background, person of color, colored skin"**

Specifications are made to avoid all sort of artifacts that the model naturally tends to introduce, such as deformed pupils, rendered or poor detailed images, along as NSFW content, despite the filter already present in the model.

## Models
The models tested were [Stable diffusion v2](https://huggingface.co/Manojb/stable-diffusion-2-base), [dreamlike-art/dreamlike-photoreal-2.0](https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0) and [stablediffusionapi/realistic-vision-v51](https://huggingface.co/stablediffusionapi/realistic-vision-v51), all based on [Stable Diffusion](https://arxiv.org/pdf/2112.10752).

The model used for the generation of the final images, the best performing one for this task, was Realistic Vision v5.1.
Specifically, the number of inference steps in the generation process and the width of the images were left to the default values, meanwhile:
- the **height** of the images was increased to obtain an aspect ratio similar to that used for ID/portrait half body photos
- the **guidance scale** was reduced to ensure a greater variation of faces, trying to keep it high enough to avoid the model ignoring important details specified in the prompt

The actual values are provided in [info.xlsx](https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/info.xlsx) and already set in the [script](https://github.com/LucaCorvitto/VDM-on-deepfake-faces/blob/main/main.py).
