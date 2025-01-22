import cv2
import tkinter as tk
from tkinter import filedialog

def upload_image():

    try:
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
        if not filepath:
            return None  # Return None if the user cancels the file dialog
        image = cv2.imread(filepath)
        return image, filepath
    except Exception as e:
        print(f"Error during file upload: {e}")
        return None, None  # Return None if an error occurs
