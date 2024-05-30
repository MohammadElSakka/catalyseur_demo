from apis.stable_difuffusion_api import generate_image_api
from apis.gemma_2b_instruct_api import generate_add_text

import base64 
import io
from PIL import Image
#A helper function to convert the PIL image to base64
#so you can send it to the API


def generate_image_controller(prompt):
    output_image = generate_image_api(prompt)
    output_text = generate_add_text(prompt)
    return [output_image, output_text]