import gradio as gr

from controllers import generate_image_controller

def welcome(name):
    return f"Hello {name}!"

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output and press enter when ready.
    """)
    inp = gr.Textbox(placeholder="What do you want?")
    out = gr.Textbox()
    inp.submit(welcome, inp, out)

    # gr.Image(generate_image_controller(inp), label="Generated image")

if __name__ == "__main__":
    demo.launch()
 