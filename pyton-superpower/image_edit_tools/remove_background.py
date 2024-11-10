from PIL import Image
from rembg import remove

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

    print(f'Background removed successfully: {input_path}')
