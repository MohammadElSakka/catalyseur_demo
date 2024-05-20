import gradio as gr

from controllers import generate_image_controller

def welcome(name):
    return f"Hello {name}!"

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    """)
    inp = gr.Textbox(placeholder="What do you want?")
    out = gr.Textbox()
    inp.change(generate_image_controller, inp, out)

if __name__ == "__main__":
    demo.launch()
