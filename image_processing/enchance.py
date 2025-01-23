import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_sharpening_highpassfilter(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def apply_sharpening_unsharp(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9,-1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def apply_contrast_stretching(image):
    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

def apply_histogram_equalization(image):
    if len(image.shape) == 2:  # Grayscale image
        equalized_image = cv2.equalizeHist(image)
        display_histogram(image, equalized_image)
    else:  # Color image
        image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
        equalized_image = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)
        display_histogram(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.cvtColor(equalized_image, cv2.COLOR_BGR2GRAY))
    return equalized_image

def enhance_image(image):
    while True:
        enhancement_prompt = """
        Choose the image enhancement method to apply:
        1. Sharpening
        2. Contrast Stretching
        3. Histogram Equalization
        Enter 1, 2, or 3:
        """
        chosen_enhancement = input(enhancement_prompt).strip()

        if chosen_enhancement == '1':
            return apply_sharpening(image)
        elif chosen_enhancement == '2':
            return apply_contrast_stretching(image)
        elif chosen_enhancement == '3':
            return apply_histogram_equalization(image)
        else:
            print("Invalid choice. Please try again.")

        redo = input("Do you want to redo the enhancement? (Y/n): ").strip().lower()
        if redo != 'y':
            break

def display_histogram(before, after):
    plt.figure(figsize=(12, 6))

    # Original image histogram
    plt.subplot(1, 2, 1)
    plt.hist(before.ravel(), bins=256, range=[0, 256], color='blue')
    plt.title('Histogram Before Equalization')

    # Equalized image histogram
    plt.subplot(1, 2, 2)
    plt.hist(after.ravel(), bins=256, range=[0, 256], color='red')
    plt.title('Histogram After Equalization')

    plt.show()
