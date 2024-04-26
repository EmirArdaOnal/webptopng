import os
from PIL import Image

def convert_webp_to_png(webp_folder, png_folder):
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)
    
    webp_files = [f for f in os.listdir(webp_folder) if f.endswith('.webp')]
    
    for webp_file in webp_files:
        webp_path = os.path.join(webp_folder, webp_file)
        
        png_path = os.path.join(png_folder, os.path.splitext(webp_file)[0] + '.png')
        
        with Image.open(webp_path) as image:
            image.save(png_path, 'PNG')

convert_webp_to_png('webpklasoru', 'pngklasoru')
