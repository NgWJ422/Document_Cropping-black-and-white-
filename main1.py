import image_processing as ip

def process_image(image):
    ip.Display(image)
    # Convert to Grayscale
    image = ip.convert_to_grayscale(image)
    ip.Display(image)
    
    # Apply Contrast Stretching
    image = ip.apply_contrast_stretching(image)
    ip.Display(image)
    
    print("Image processing completed: Grayscale and Contrast Stretching applied.")
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
        
    ip.compress_and_save(cropped_image, filepath, ".jpg")

if __name__ == "__main__":
    main()
