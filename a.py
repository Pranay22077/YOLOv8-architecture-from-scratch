import json, base64, os

with open("yolov8-003.ipynb", "r") as f:
    data = json.load(f)

os.makedirs("extracted_images", exist_ok=True)
count = 0

for cell in data.get("cells", []):
    attachments = cell.get("attachments", {})
    for name, content in attachments.items():
        img_data = content.get("image/png", "")
        if img_data:
            with open(f"extracted_images/{name}", "wb") as img_file:
                img_file.write(base64.b64decode(img_data))
            count += 1

print(f"Extracted {count} images from attachments into 'extracted_images/' folder.")
