import os
from PIL import Image

# --- CONFIGURATION ---
input_folder = "input_images"
output_folder = "output_images"
resize_width = 800
resize_height = 600
output_format = "JPEG"  # Options: "JPEG", "PNG", etc.

# --- CREATE OUTPUT FOLDER IF NOT EXISTS ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- PROCESS ALL IMAGES IN FOLDER ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        print(f"Processing: {filename}")

        # Open and resize
        with Image.open(img_path) as img:
            img_resized = img.resize((resize_width, resize_height))

            # Convert & Save
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img_resized.save(output_path, output_format)

        print(f"Saved resized image: {output_path}")

print("\n All images have been resized and saved to:", output_folder)
