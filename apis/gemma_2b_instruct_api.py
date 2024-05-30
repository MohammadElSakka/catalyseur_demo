import requests
import json

API_URL_GENERATION = "https://api-inference.huggingface.co/models/google/gemma-1.1-2b-it"
headers = {"Authorization": "Bearer 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"}


def query(payload):
	response = requests.post(API_URL_GENERATION, headers=headers, json=payload)
	return response.content
def generate_add_text(input_):

    
    output = query(
        {
        'inputs':f"make a advertisement description of this: {input_} ##",
        'parameters':{
            'return_full_text':False,
            'max_new_tokens' :500
            }
        }
    )
    output = json.loads(output)
    return output[0]['generated_text']