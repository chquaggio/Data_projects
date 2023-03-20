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

#function to read inputs, manipulate them and deliver outputs
def reader(pos_prompts, neg_prompts, num_outputs, prompt_strength, num_inference_steps, guidance_scale, image):
    save_img(image)
    inputs['prompt'] = pos_prompts
    inputs['negative_prompt'] = neg_prompts
    inputs['input_image'] = open('/home/dev/Data_projects/gradio/my_image_input.png', 'rb') 
    inputs['num_outputs'] = num_outputs
    inputs['num_inference_steps'] = num_inference_steps
    inputs['prompt_strength'] = prompt_strength
    inputs['guidance_scale'] = guidance_scale
    inputs['scheduler'] = 'DPMSolverMultistep'

    output = version.predict(**inputs)
    gallery = []
    for i in range(num_outputs):
        response = requests.get(output[i])
        gallery.append(PIL.Image.open(BytesIO(response.content)))

    return gallery

#definitionof the interface
demo = gr.Interface(
    fn=reader,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your positive prompts here (comma separated)"), 
            gr.Textbox(lines=2, placeholder="Enter your negative prompts here (comma separated)"), 
            gr.Slider(1, 8, step=1), 
            gr.Slider(0, 1, step=0.05), 
            gr.Slider(1, 500), 
            gr.Slider(1, 20),
            "image"],
    outputs=[gr.Gallery(label="Generated images", show_label=True).style(grid=[2], height="auto")],
    )
demo.launch(share=True, server_name="0.0.0.0")

