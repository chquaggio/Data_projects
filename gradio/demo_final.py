import gradio as gr
import replicate
import requests
import PIL
from matplotlib import cm
import numpy as np
import sys
from io import BytesIO

model = replicate.models.get("jagilley/stable-diffusion-depth2img")
version = model.versions.get("68f699d395bc7c17008283a7cef6d92edc832d8dc59eb41a6cafec7fc70b85bc")
inputs = {}
def save_img(npa):
    im = PIL.Image.fromarray(npa.astype('uint8'), 'RGB')
    im.save("my_image_input.png")
#inputs = {
#	'prompt': xx,
#	'negative_prompt': xx,
#	'input_image': open("path/to/image", "rb"),
#	'prompt_strength': xx
#	'num_outputs': 1,
#	'num_inference_steps': xx,
#	'guidance_scale': xx,
#	'scheduler': 'DPMSolverMultistep'
#}

#function to read inputs, manipulate them and deliver outputs
def reader(pos_prompts, neg_prompts, prompt_strength, num_inference_steps, guidance_scale, image):
    save_img(image)
    inputs['prompt'] = pos_prompts
    inputs['negative_prompt'] = neg_prompts
    inputs['input_image'] = open('/home/dev/Data_projects/gradio/my_image_input.png', 'rb') 
    inputs['num_outputs'] = 1
    inputs['num_inference_steps'] = num_inference_steps
    inputs['prompt_strength'] = prompt_strength
    inputs['guidance_scale'] = guidance_scale
    inputs['scheduler'] = 'DPMSolverMultistep'

    output = version.predict(**inputs)
    response = requests.get(output[0])

    return PIL.Image.open(BytesIO(response.content))

#definitionof the interface
demo = gr.Interface(
    fn=reader,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your positive prompts here (comma separated)"), gr.Textbox(lines=2, placeholder="Enter your negative prompts here (comma separated)"), gr.Slider(0, 1, step=0.05), gr.Slider(1, 500), gr.Slider(1, 20),"image"],
    outputs=["image"],
    )
demo.launch(server_name="0.0.0.0")

