import cv2
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import os
from .display import Display

def getImagefilesize(image):
    """Helper function to display an image using OpenCV and show its size."""
    # Save the image temporarily to get its file size
    temp_filename = "temp_image.jpg"
    cv2.imwrite(temp_filename, image)
    
    # Get file size in KB
    file_size = os.path.getsize(temp_filename) / 1024  # Convert to KB

    # Clean up temporary file
    os.remove(temp_filename)

    return file_size

def chroma_downsampling(image):
    """
    Apply chroma downsampling based on user-specified ratio.
    
    Args:
        image (numpy.ndarray): Input BGR image.
    
    Returns:
        numpy.ndarray: Chroma downsampled image.
    """
    # Prompt the user to choose a chroma subsampling ratio
    prompt = """
    Choose a chroma subsampling ratio:
    1. 4:4:4 (No subsampling)
    2. 4:2:2 (Horizontal chroma subsampling)
    3. 4:2:0 (Horizontal and vertical chroma subsampling)
    4. 4:1:1 (Extreme horizontal chroma subsampling)
    Enter your choice (1/2/3/4): 
    """
    choice = input(prompt)
    
    # Map user choice to subsampling ratio
    ratio_map = {
        "1": "4:4:4",
        "2": "4:2:2",
        "3": "4:2:0",
        "4": "4:1:1"
    }
    ratio = ratio_map.get(choice)
    if not ratio:
        raise ValueError("Invalid choice. Please select a valid option.")
    
    # Convert to YCbCr color space
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    
    # Split the Y, Cb, Cr channels
    y, cb, cr = cv2.split(ycrcb)
    
    if ratio == "4:4:4":
        # No subsampling
        cb_downsampled, cr_downsampled = cb, cr
    
    elif ratio == "4:2:2":
        # Horizontal downsampling of chroma channels
        cb_downsampled = cb[:, ::2]
        cr_downsampled = cr[:, ::2]
    
    elif ratio == "4:2:0":
        # Horizontal and vertical downsampling of chroma channels
        cb_downsampled = cb[::2, ::2]
        cr_downsampled = cr[::2, ::2]
    
    elif ratio == "4:1:1":
        # Reduce horizontal resolution of chroma channels to 1/4th
        cb_downsampled = cb[:, ::4]
        cr_downsampled = cr[:, ::4]
    
    # Upsample chroma channels back to original size
    cb_upsampled = cv2.resize(cb_downsampled, (cb.shape[1], cb.shape[0]), interpolation=cv2.INTER_LINEAR)
    cr_upsampled = cv2.resize(cr_downsampled, (cr.shape[1], cr.shape[0]), interpolation=cv2.INTER_LINEAR)
    
    # Merge the Y channel with the upsampled Cb and Cr channels
    ycrcb_downsampled = cv2.merge([y, cb_upsampled, cr_upsampled])
    
    # Convert back to BGR color space
    downsampled_image = cv2.cvtColor(ycrcb_downsampled, cv2.COLOR_YCrCb2BGR)
    
    return downsampled_image


def apply_compression(image, file_extension):
    """Apply compression based on the user-selected format and parameters."""
    if file_extension.lower() == '.jpg':
        quality = int(input("Enter the JPEG quality (0-100, recommended 90): "))
        compressed_image = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])[1]
        compressed_image = cv2.imdecode(compressed_image, cv2.IMREAD_COLOR)  # Decode back to image
    elif file_extension.lower() == '.png':
        compression_level = int(input("Enter the PNG compression level (0-9, recommended 3): "))
        compressed_image = cv2.imencode('.png', image, [int(cv2.IMWRITE_PNG_COMPRESSION), compression_level])[1]
        compressed_image = cv2.imdecode(compressed_image, cv2.IMREAD_COLOR)  # Decode back to image
    elif file_extension.lower() == '.jpg_chroma':
        print("Applying chroma downsampling...")
        compressed_image = chroma_downsampling(image)
    else:
        print("No compression applied for this format.")
        compressed_image = image
    return compressed_image

def save_image(image, original_path, file_extension):
    """Function to save the image with user-selected compression settings."""
    base_name = original_path.split('/')[-1].split('.')[0]
    default_name = f"{base_name}_compressed{file_extension}"
    
    # Lock the file type based on the compression format
    if file_extension == '.jpg' or file_extension == '.jpg_chroma':
        filetypes = [("JPEG", "*.jpg")]
    elif file_extension == '.png':
        filetypes = [("PNG", "*.png")]
    else:
        # Fallback case (shouldn't reach here with proper logic)
        filetypes = [("All files", "*.*")]
    
    save_path = filedialog.asksaveasfilename(
        defaultextension=file_extension, 
        filetypes=filetypes,  # Lock file type to the chosen compression format
        initialfile=default_name  # Default file name
    )

    if save_path:
        cv2.imwrite(save_path, image)
        print(f"Image saved to {save_path}")
    else:
        print("Save operation canceled.")


def compress_and_save(image, original_path, files_extension = None):
    """Main function to ask the user for compression settings and save the image."""
    
    while True:
        file_extension = files_extension
        # Prompt for file format to save
        if(file_extension is None):
            number = input("""
            Enter the image format to save (e.g., .jpg, .png, .jpg_chroma for chroma downsampling):
            1. .jpg
            2. .png
            3. .jpg_chroma (for chroma downsampling)
            Please enter the number corresponding to your choice: """)
            
            # Map user input to file extension
            if number == '1':
                file_extension = '.jpg'
            elif number == '2':
                file_extension = '.png'
            elif number == '3':
                file_extension = '.jpg_chroma'
            else:
                print("Invalid choice, using .jpg as default.")
                file_extension = '.jpg'
                
        # Apply compression
        compressed_image = apply_compression(image, file_extension)

        # Show file size for original image
        file_size = getImagefilesize(image)
        print(f"Original Image size: {file_size:.2f} KB")
        
        # Show the result
        file_size = getImagefilesize(compressed_image)
        Display(compressed_image)
        print(f"Compressed Image size: {file_size:.2f} KB")
        
        # Ask user for approval
        user_approval = input("Do you like this compression? (Y/N): ").strip().lower()
        
        if user_approval == 'y':
            # Save the image if the user approves
            save_image(compressed_image, original_path, file_extension)
            break
        else:
            print("You can adjust the compression settings and try again.")
            continue