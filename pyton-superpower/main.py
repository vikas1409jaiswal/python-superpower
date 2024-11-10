import os
import json
from image_edit_tools import ImageEditService

# Load configuration from a JSON file
def load_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def main():
    # Load the configuration
    config = load_config()

    # Set up image editing service with default crop percentages
    image_service = ImageEditService()

    # Get current directory and valid extensions
    current_dir = os.path.dirname(os.path.abspath(__file__))
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.tiff')

    # Process each image in the current directory
    for file_name in os.listdir(current_dir):
        if file_name.lower().endswith(valid_extensions):
            input_path = os.path.join(current_dir, file_name)
            output_path = input_path.lower().replace('.jpg', '.png').replace(' ', '-')

            if config.get('remove_bg', False):
                image_service.remove_background(input_path, output_path)

            if config.get('crop', False):
                crop_percentages = config.get('crop_percentages', (0, 0, 0, 0))
                cropped_output_path = output_path.replace('.jpg', '_cropped.jpg')
                image_service.crop_image(input_path, cropped_output_path, crop_percentages)

if __name__ == "__main__":
    main()

