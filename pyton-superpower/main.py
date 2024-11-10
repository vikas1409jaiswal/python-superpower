# main.py
import os
from image_edit_tools import remove_background, crop_image

# Define the crop percentages globally if used repeatedly
CROP_PERCENTAGES = (0.2, 0, 0.85, 0.6)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.tiff')

    for file_name in os.listdir(current_dir):
        if file_name.lower().endswith(valid_extensions):
            input_path = os.path.join(current_dir, file_name)
            output_path = input_path.lower().replace('.jpg', '.png').replace(' ',
                                                                             '-')  # Save cropped image to the same file
            # Crop the image
            cropped_path = input_path.replace('.jpg', '_cropped.jpg')  # Change the file extension if needed
            crop_image(input_path, cropped_path, CROP_PERCENTAGES)

            # Remove background from cropped image
            # remove_background(input_path, output_path)


if __name__ == "__main__":
    main()
