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

#definition of the block
block = gr.Blocks().queue()
with block:
    with gr.Row():
        with gr.Column():
            image = gr.Image(source='upload')
            pos_prompts = gr.Textbox(lines=2, placeholder="Enter your positive prompts here (comma separated)")
            neg_prompts = gr.Textbox(lines=2, placeholder="Enter your negative prompts here (comma separated)")
            run_button = gr.Button(label="Run")
            with gr.Accordion("Advanced options", open=False):
                num_outputs = gr.Slider(
                    label="Images", minimum=1, maximum=4, value=1, step=1)
                num_inference_steps = gr.Slider(label="Steps", minimum=1,
                                       maximum=50, value=50, step=1)
                guidance_scale = gr.Slider(
                    label="Guidance Scale", minimum=0.1, maximum=30.0, value=9.0, step=0.1)
                prompt_strength = gr.Slider(
                    label="Strength", minimum=0.0, maximum=1.0, value=0.9, step=0.01)
        with gr.Column():
            gallery = gr.Gallery(label="Generated images", show_label=False).style(grid=[2], height="auto")

    run_button.click(fn=reader, inputs=[pos_prompts, neg_prompts, num_outputs, prompt_strength, num_inference_steps, guidance_scale, image], outputs=[gallery])


block.launch(server_name="0.0.0.0")







