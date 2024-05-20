import requests
import io
import numpy as np

API_URL = "https://api-inference.huggingface.co/models/sd-dreambooth-library/fashion"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_image_api(inputs):
	image_bytes = query({
		"inputs": inputs,
	})

	return np.frombuffer(io.BytesIO(image_bytes), dtype=np.float32)