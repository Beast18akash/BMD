import os
import glob

root_dir = r"c:\Users\holsa\Downloads\PetCare-main\PetCare-main"

for filepath in glob.glob(os.path.join(root_dir, "**/*.html"), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace header logo size
    content = content.replace('style="height: 50px; vertical-align: middle;"', 'style="height: 80px; vertical-align: middle;"')
    
    # Replace footer logo size
    content = content.replace('style="height: 60px; vertical-align: middle; margin-bottom: 15px;"', 'style="height: 100px; vertical-align: middle; margin-bottom: 15px;"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print("Logo size increased successfully.")
