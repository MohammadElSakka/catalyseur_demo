import gradio as gr
from controllers import generate_image_controller


import gradio as gr

from controllers import generate_image_controller
generate_image_controller('nice leather jacket')
with gr.Blocks() as demo:
    gr.Markdown(value='# **Fast Fashion addvertisment with Generative AI**')
    user_prompt = gr.Textbox(label='Please, introduce your fashion idea in English', placeholder='Beautiful snake leather boots',min_width=512)
    generation_bottom = gr.Button(value='Generate fashion!')
    
    with gr.Row(equal_height=True) as r:

        
        generated_image = gr.Image(label='Fashion image',height=512, width=512)
        generated_text = gr.Markdown(label='Fashion text')
        generation_bottom.click(
                                fn=generate_image_controller,
                                inputs=[user_prompt],
                                outputs=[generated_image, generated_text]
                                )
    clear = gr.ClearButton(components=[generated_image, generated_text])
gr.close_all()
demo.launch()

if __name__ == "__main__":
    demo.launch()
 