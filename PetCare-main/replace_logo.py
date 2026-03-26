import os
import glob
import re

root_dir = r"c:\Users\holsa\Downloads\PetCare-main\PetCare-main"

for filepath in glob.glob(os.path.join(root_dir, "**/*.html"), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine relative path to assets folder
    if 'pages' in os.path.normpath(filepath).split(os.sep):
        img_src = "../assets/logo.png"
    else:
        img_src = "./assets/logo.png"

    # Replace header logo
    old_header_logo = r'<a href="[^"]*index\.html" class="logo"><i class="fa-solid fa-paw"></i>Pet<span>Care</span></a>'
    new_header_logo = f'<a href="./index.html" class="logo"><img src="{img_src}" alt="PetCare Logo" style="height: 50px; vertical-align: middle;"></a>'
    if 'pages' in os.path.normpath(filepath).split(os.sep):
        new_header_logo = new_header_logo.replace('href="./index.html"', 'href="../index.html"')
    
    content = re.sub(old_header_logo, new_header_logo, content)

    # Replace footer logo
    old_footer_logo = r'<h3><i class="fa-solid fa-paw"></i>Pet<span>Care</span></h3>'
    new_footer_logo = f'<h3><img src="{img_src}" alt="PetCare Logo" style="height: 60px; vertical-align: middle; margin-bottom: 15px;"></h3>'
    
    content = re.sub(old_footer_logo, new_footer_logo, content)

    # Fix smart quotes
    content = content.replace("href=”#”", 'href="#"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML updates applied successfully.")
