import requests
import io
from PIL import Image
API_URL_DIFUSSION = "https://api-inference.huggingface.co/models/sd-dreambooth-library/fashion"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL_DIFUSSION, headers=headers, json=payload)
	return response.content

def generate_image_api(inputs):
	image_bytes = query({
		"inputs": inputs,
		'parameters': {
			'guidance_scale': 9, # How closely follows the prompt
			'num_inference_steps':100 #steps for the denoising process. the higher, the better. 100 is ok for the demo.
        }
	})

	return Image.open(io.BytesIO(image_bytes))