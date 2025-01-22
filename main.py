import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np
import image_processing as ip

def main():
    while True:
        # Upload an image
        try:
            image_BRG, filepath = ip.upload_image()
            ip.Display(image_BRG)
        except Exception as e:
            print(e)
            print("Program canceled.")
            return  # Exit the program gracefully

        # Convert the image to grayscale/Black and White
        image = ip.ChangeWhich(image_BRG)
        ip.Display(image)

        # Denoise the image
        image = ip.Denoise(image)
        ip.Display(image)

        # Enhance the image
        image = ip.Enhance(image)
        ip.Display(image)

        # Crop the image
        cropped_image, filepath = ip.ImgCrop(image, filepath)
        if cropped_image.size > 0:
            break
        else:
            continue

    ip.compress_and_save(cropped_image, filepath)



if __name__ == "__main__":
    main()
