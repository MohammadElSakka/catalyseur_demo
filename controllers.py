from apis.stable_difuffusion_api import generate_image_api

def generate_image_controller(request):
    output_bytes = generate_image_api(request)
    return f'Your request: {request} received the output (Bytes): {output_bytes}'