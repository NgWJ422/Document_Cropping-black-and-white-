### DOCUMENT CROPPING
DIP assignment by Ng Wei Jie, Wee Mao Phin, Hee Yee Cinn, Goh Jia Xuen

## For Dr:
The program main1.py is the program for user, which when run will is the one that will prompt the user to select an image, then crop it, after that the program will process the image by grayscale it, and do contrast stretching. Then, the image will be compressed using JPEG compression with user's choosen quality. Finally, user can save the image. 


## Overview
This project provides a complete pipeline for cropping and processing images, aimed at tasks such as document digitization or preprocessing for OCR systems. It leverages OpenCV for image manipulation and Tkinter for user interaction. The program includes modules for image uploading, cropping, denoising, enhancement, and compression.

## Features
1. **Image Upload**: Allows users to select an image file via a graphical file dialog.
2. **Image Cropping**: Provides an intuitive interface for selecting regions of interest (ROI).
3. **Grayscale Conversion**: Converts the cropped image to grayscale or black and white.
4. **Image Denoising**: Reduces noise using various techniques such as Non-Local Means, Median Filtering, and Gaussian Blur.
5. **Image Enhancement**: Enhances image quality with sharpening, contrast stretching, or histogram equalization.
6. **Compression**: Saves the processed image with chroma subsampling for reduced file size.

## Installation
1. **Prerequisites**:
   - Python 3.8 or later.
   - Required Python libraries:
     ```bash
     pip install opencv-python numpy matplotlib screeninfo
     ```
2. **Download**:
   Clone the repository or download the source code.

3. **Run**:
   Navigate to the project directory and execute the main script:
   ```bash
   python main.py
   ```

## Usage
1. Run the program: `python main.py`.
2. Follow the prompts to upload an image.
3. Use the provided GUI tools to crop the image and apply enhancements.
4. View and interact with the image at various stages of processing.
5. Save the processed image with optional compression.

## Project Structure
- **`main.py`**: The main script controlling the program flow.
- **`upload.py`**: Handles file selection and image loading.
- **`crop.py`**: Provides cropping functionality and screen resolution adjustments.
- **`display.py`**: Handles image visualization, resizing, and display.
- **`denoise.py`**: Implements denoising techniques.
- **`enhance.py`**: Includes image enhancement methods like sharpening, contrast stretching, and histogram equalization.
- **`compress_and_save.py`**: Manages image compression and saving with chroma subsampling.

## Key Functions
### Image Upload
- Opens a file dialog to select an image.
- Supports common formats like JPG, PNG, BMP, and TIFF.

### Image Cropping
- Resizes the image based on screen dimensions for better usability.
- Allows users to interactively select the region of interest.

### Image Enhancement
- Sharpening: Applies a kernel to emphasize details.
- Contrast Stretching: Normalizes pixel intensity for better contrast.
- Histogram Equalization: Enhances brightness and contrast based on image histograms.

### Image Denoising
- Non-Local Means: Reduces noise while preserving details.
- Median Filtering: Removes salt-and-pepper noise.
- Gaussian Blur: Smoothens the image to reduce high-frequency noise.

### Compression
- Supports chroma subsampling ratios (4:4:4, 4:2:2, 4:2:0, 4:1:1).
- Reduces file size for efficient storage.

## Example Workflow
1. **Upload an Image**: Select an image from your device.
2. **Crop the Image**: Define the area to retain using an interactive GUI.
3. **Enhance the Image**: Choose enhancement methods based on requirements.
4. **Denoise the Image**: Apply a preferred denoising technique.
5. **Save the Image**: Compress and save the final image.

## Future Improvements
- Add more advanced enhancement techniques, such as deep learning-based super-resolution.
- Implement batch processing for multiple images.
- Provide a GUI for the entire workflow.

