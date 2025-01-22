import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np
from screeninfo import get_monitors

# Function to get the screen resolution of the primary monitor
def get_screen_size():
    monitor = get_monitors()[0]  # Get the primary monitor
    return monitor.width, monitor.height

# Function to crop an image
def crop_image(image, max_width, max_height):
    # Get the current dimensions of the image
    height, width = image.shape[:2]
    
    # Calculate scaling factors to keep the aspect ratio
    scaling_factor = min(max_width / width, max_height / height)
    
    # Resize image if it exceeds the max width or height
    if scaling_factor < 1:
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        image = cv2.resize(image, (new_width, new_height))

    # Display the resized image for cropping
    r = cv2.selectROI("Select Crop Area", image, showCrosshair=True, fromCenter=False)
    
    # Crop the image based on the ROI selected
    cropped_image = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.destroyAllWindows()
    return cropped_image


def imgCrop(image=None, filepath=None):
    # Get the screen resolution of the primary monitor
    screen_width, screen_height = get_screen_size()
    
    # Define a margin and set the max dimensions based on screen resolution
    margin = 100
    max_width = screen_width - margin
    max_height = screen_height - margin
    
    # Crop the image
    return crop_image(image, max_width, max_height), filepath
    