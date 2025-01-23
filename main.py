import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np
import image_processing as ip

def process_image(image):
    while True:
        processing_prompt = """
        Choose the image processing technique to apply:
        1. Convert to Black and White
        2. Convert to Black and White (Adaptive)
        3. Convert to Grayscale
        4. Apply Gaussian Blur
        5. Apply Median Filtering
        6. Apply Non-Local Means Denoising
        7. Apply Contrast Stretching
        8. Apply Histogram Equalization
        9. Apply Sharpening(high pass filter)
        10. Apply Sharpening(unsharp mask)
        Enter the number corresponding to your choice, or 'q' to quit:
        """
        choice = input(processing_prompt).strip()

        if choice == '1':
            image = ip.convert_to_black_and_white(image)
        elif choice == '2':
            image = ip.convert_to_black_and_white_adaptive(image)
        elif choice == '3':
            image = ip.convert_to_grayscale(image)
        elif choice == '4':
            image = ip.apply_gaussian_blur(image)
        elif choice == '5':
            image = ip.apply_median_filtering(image)
        elif choice == '6':
            image = ip.apply_non_local_means_denoising(image)
        elif choice == '7':
            image = ip.apply_contrast_stretching(image)
        elif choice == '8':
            image = ip.apply_histogram_equalization(image)
        elif choice == '9':
            image = ip.apply_sharpening_highpassfilter(image)
        elif choice == "10":
            image = ip.apply_sharpening_unsharp(image)
        elif choice.lower() == 'q':
            print("Exiting image processing.")
            break
        else:
            print("Invalid choice. Please try again.")
        ip.Display(image)
    return image

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
        break
    cropped_image = process_image(cropped_image)
        
    ip.compress_and_save(cropped_image, filepath)



if __name__ == "__main__":
    main()
