from PIL import Image

def crop_image(input_path, output_path, crop_percentages):
    with Image.open(input_path) as img:
        width, height = img.size
        left = width * crop_percentages[0]
        top = height * crop_percentages[1]
        right = width * crop_percentages[2]
        bottom = height * crop_percentages[3]

        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path)

        print(f'Image cropped successfully: {input_path}')
