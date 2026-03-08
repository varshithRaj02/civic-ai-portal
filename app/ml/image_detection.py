from PIL import Image
import os

def detect_image_risk(image_path):

    try:

        if not os.path.exists(image_path):
            return "No Image"

        img = Image.open(image_path)
        img.verify()

        return "Potential Hazard"

    except Exception as e:

        print("Image detection error:", e)
        return "Unknown"