import cv2
import numpy as np
import matplotlib.pyplot as plt

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
            # Sharpening using a kernel
            kernel = np.array([[0, -1, 0],
                               [-1, 5,-1],
                               [0, -1, 0]])
            sharpened_image = cv2.filter2D(image, -1, kernel)
            return sharpened_image

        elif chosen_enhancement == '2':
            # Contrast stretching
            min_val = np.min(image)
            max_val = np.max(image)
            contrast_stretched_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
            return contrast_stretched_image

        elif chosen_enhancement == '3':
            # Histogram equalization
            if len(image.shape) == 2:  # Grayscale image
                equalized_image = cv2.equalizeHist(image)
                display_histogram(image, equalized_image)
            else:  # Color image
                image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
                image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])
                equalized_image = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)
                display_histogram(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), cv2.cvtColor(equalized_image, cv2.COLOR_BGR2GRAY))
            return equalized_image

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
