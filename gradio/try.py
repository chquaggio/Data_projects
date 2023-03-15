import gradio as gr
import replicate

model = replicate.models.get("jagilley/stable-diffusion-depth2img")
version = model.versions.get("68f699d395bc7c17008283a7cef6d92edc832d8dc59eb41a6cafec7fc70b85bc")
inputs = {
	'prompt': 'digital art',
	'negative_prompt': 'medieval art',
	'input_image': open("/home/dev/Data_projects/gradio/cq.png", "rb"),
	'prompt_strength': 0.6,
	'num_outputs': 1,
	'num_inference_steps': 50,
	'guidance_scale': 7.5,
	'scheduler': 'DPMSolverMultistep'
}

output = version.predict(**inputs)
print(output[0])
