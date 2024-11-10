import os
from PIL import Image
from rembg import remove

class ImageEditService:
    def __init__(self, crop_percentages=(0.2, 0, 0.85, 0.6)):
        self.crop_percentages = crop_percentages

    def remove_background(self, input_path, output_path):
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

        print(f'Background removed successfully: {input_path}')

    def crop_image(self, input_path, output_path, crop_percentages):
        with Image.open(input_path) as img:
            width, height = img.size
            left = width * crop_percentages[0]
            top = height * crop_percentages[1]
            right = width * crop_percentages[2]
            bottom = height * crop_percentages[3]

            img_cropped = img.crop((left, top, right, bottom))
            img_cropped.save(output_path)

            print(f'Image cropped successfully: {input_path}')
