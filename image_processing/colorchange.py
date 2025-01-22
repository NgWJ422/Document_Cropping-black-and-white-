import cv2

def convert_to_black_and_white(image):
    threshold_value = int(input("Threshold value(normally: 127): "))
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    binary_BRG_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    
    return binary_BRG_image


def convert_to_black_and_white_adaptive(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    binary_image = cv2.adaptiveThreshold(
        gray_image,       # Grayscale image
        255,              # Maximum value (white)
        cv2.ADAPTIVE_THRESH_MEAN_C,  # Adaptive method (mean of neighborhood area)
        cv2.THRESH_BINARY,         # Binary thresholding
        11,                # Block size (area around each pixel to compute threshold)
        2                  # Constant subtracted from the mean to adjust threshold
    )
    binary_BRG_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)

    return binary_BRG_image


def convert_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale_BRG_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)
    return grayscale_BRG_image

def changeWhich(image):
    prompt = """
          
Which color change would you like to make?
    1. Convert to Black and White
    2. Convert to Black and White (Adaptive)
    3. Convert to Grayscale
          
Please enter the number of your choice.
    """
    choice = input(prompt)
    if choice == "1":
        return convert_to_black_and_white(image)
    elif choice == "2":
        return convert_to_black_and_white_adaptive(image)
    elif choice == "3":
        return convert_to_grayscale(image)
    else:
        print("Invalid choice. Please try again.")
        return changeWhich(image)