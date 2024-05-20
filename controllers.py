from apis.stable_difuffusion_api import generate_image_api

def generate_image_controller(request):
    output_image = generate_image_api(request)
    return output_image