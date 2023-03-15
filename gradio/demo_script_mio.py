import gradio as gr

def naive_reader(pos_prompts, neg_prompts, check_param, slide_param, image):
    pp = pos_prompts.split(',')
    np = neg_prompts.split(',')
    list_p = "First two positive prompts:{}, {}".format(pp[0], pp[1])
    list_np = "First two negative prompts:{}, {}".format(np[0], np[1])
    cp = "check_param is {}".format(check_param)
    sp = "slide_param is {}".format(slide_param)
    return list_p, list_np, cp, sp, image

demo = gr.Interface(
    fn=naive_reader,
    inputs=[gr.Textbox(lines=2, placeholder="Enter your positive prompts here (comma separated)"), gr.Textbox(lines=2, placeholder="Enter your negative prompts here (comma separated)"), "checkbox", gr.Slider(0, 100), "image"],
    outputs=["text", "text", "text", "text", "image"],
    )
demo.launch(server_name="0.0.0.0")

