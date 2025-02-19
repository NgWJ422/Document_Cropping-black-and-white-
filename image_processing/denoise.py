import cv2

def apply_non_local_means_denoising(image):
    h = int(input("Enter the h parameter (recommended 10): ").strip())
    templateWindowSize = int(input("Enter the templateWindowSize (recommended 7): ").strip())
    searchWindowSize = int(input("Enter the searchWindowSize (recommended 21): ").strip())
    return cv2.fastNlMeansDenoising(image, None, h=h, templateWindowSize=templateWindowSize, searchWindowSize=searchWindowSize)

def apply_median_filtering(image):
    while True:
        ksize = int(input("Enter the kernel size for Median Filtering (odd number, recommended 5): ").strip())
        if ksize % 2 == 0:
            print("Kernel size must be an odd number.")
            continue
        return cv2.medianBlur(image, ksize=ksize)

def apply_gaussian_blur(image):
    while True:
        kernel_size = int(input("Enter the kernel size for Gaussian Blur (odd number, recommended 5): ").strip())
        if kernel_size % 2 == 0:
            print("Kernel size must be an odd number.")
            continue
        sigmaX = float(input("Enter the sigmaX parameter for Gaussian Blur (recommended 1.0): ").strip())
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX=sigmaX)

def Denoise(image):
    while True:
        selection_prompt = """
        Choose the denoising method to use for deconvolution:
        1. Non-Local Means Denoising
        2. Median Filtering
        3. Gaussian Blur
        Enter 1, 2, or 3:
        """
        chosen_denoised_image = input(selection_prompt).strip()

        if chosen_denoised_image == '1':
            return apply_non_local_means_denoising(image)
        elif chosen_denoised_image == '2':
            return apply_median_filtering(image)
        elif chosen_denoised_image == '3':
            return apply_gaussian_blur(image)
        else:
            print("Invalid choice. Please try again.")

        redo = input("Do you want to redo the denoising? (Y/n): ").strip().lower()
        if redo != 'y':
            break
