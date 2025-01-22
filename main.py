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
        except Exception as e:
            print("Program canceled.")
            return  # Exit the program gracefully

        # Crop the image
        cropped_image, filepath = ip.ImgCrop(image_BRG, filepath)
        if cropped_image.size <= 0:
            continue

        # Convert the image to grayscale/Black and White
        cropped_image = ip.ChangeWhich(cropped_image)
        ip.Display(cropped_image)

        # Denoise the image
        cropped_image = ip.Denoise(cropped_image)
        ip.Display(cropped_image)

        # Enhance the image
        cropped_image = ip.Enhance(cropped_image)
        ip.Display(cropped_image)

        break

    ip.compress_and_save(cropped_image, filepath)



if __name__ == "__main__":
    main()
