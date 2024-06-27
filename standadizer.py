from PIL import Image
import os

def resize_and_standardize_images(input_dir, output_dir, size=(128, 128)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        try:
            if filename.endswith((".jpg", ".png", ".jpeg","JPG","bmp","PNG")):  # Added ".jpeg" to the tuple
                print(f"Processing {filename}")
                img = Image.open(os.path.join(input_dir, filename))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                img = img.resize(size, Image.LANCZOS)
                img = img.convert('RGB')
                img.save(os.path.join(output_dir, filename))
        except Exception as e:
            print(f"Error processing {filename}: {e}")


# Usage
input_dir = "C:\\Users\\sharon\\Desktop\\dom\\dataset\\train\\non_standadized"
output_dir = "C:\\Users\\sharon\\Desktop\\dom\\dataset\\train\\normal_baby"
resize_and_standardize_images(input_dir, output_dir)
