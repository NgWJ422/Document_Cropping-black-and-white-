import cv2
from .crop import get_screen_size
def Display(image):
    # Get screen size
    max_width , max_height = get_screen_size()
    
    # Get the current dimensions of the image
    height, width = image.shape[:2]
    
    # Calculate scaling factors to keep the aspect ratio
    scaling_factor = min(max_width / width, max_height / height)
    
    # Resize image if it exceeds the max width or height
    if scaling_factor < 1:
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        image = cv2.resize(image, (new_width, new_height))
    
    # Display the image using cv2.imshow
    cv2.imshow("Image", image)
    
    # Wait for a key press to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()