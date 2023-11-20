import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display images and histograms using matplotlib
def display_image_with_histogram(image, title, histogram, save_path=None):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].imshow(image, cmap='gray' if len(image.shape) == 2 else None)
    axs[0].set_title(title)
    axs[0].axis('off')

    axs[1].plot(histogram, color='black', linewidth=2)
    axs[1].set_title('Histogram')
    axs[1].set_xlim([0, 256])
    axs[1].set_ylim([0, 5000])  # Adjusted y-axis scale to 1000
    axs[1].grid(True, linestyle='--', alpha=0.7)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# Read an image from file
image_path = '/mnt/6EAA986CAA983297/python/img.jpg'
original_image = cv2.imread(image_path)

# Convert the original image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_gray_image = cv2.GaussianBlur(gray_image, (15, 15), 0)

# Apply edge detection using Canny to the grayscale image
edges_gray = cv2.Canny(blurred_gray_image, 50, 150)

# Save grayscale images
cv2.imwrite('/mnt/6EAA986CAA983297/python/processedImages/gray_original_image.jpg', gray_image)
cv2.imwrite('/mnt/6EAA986CAA983297/python/processedImages/gray_blurred_image.jpg', blurred_gray_image)
cv2.imwrite('/mnt/6EAA986CAA983297/python/processedImages/gray_edges.jpg', edges_gray)

# Display each grayscale image with its histogram and save them separately
display_image_with_histogram(gray_image, 'Grayscale Original Image', cv2.calcHist([gray_image], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/gray_original_image_with_histogram.jpg')

display_image_with_histogram(blurred_gray_image, 'Blurred Grayscale Image',
                              cv2.calcHist([blurred_gray_image], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/gray_blurred_image_with_histogram.jpg')

display_image_with_histogram(edges_gray, 'Edges on Grayscale Image',
                              cv2.calcHist([edges_gray], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/gray_edges_with_histogram.jpg')

# Continue with the color images and final combined image...

# Apply Gaussian blur to the original image
blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)

# Apply edge detection using Canny to the original image
edges = cv2.Canny(blurred_image, 50, 150)

# Compress the original image using JPEG compression
compression_params = [cv2.IMWRITE_JPEG_QUALITY, 90]  # Adjust quality as needed (0 to 100)
compressed_image_path = '/mnt/6EAA986CAA983297/python/processedImages/compressed_image1.jpg'
cv2.imwrite(compressed_image_path, original_image, compression_params)

# Enhance the original image by adjusting brightness and contrast
alpha = 1.5  # Contrast control (1.0 means no change)
beta = 10    # Brightness control (0 means no change)
enhanced_image = cv2.convertScaleAbs(original_image, alpha=alpha, beta=beta)

# Save the enhanced image
output_path_enhanced = '/mnt/6EAA986CAA983297/python/processedImages/enhanced_image1.jpg'
cv2.imwrite(output_path_enhanced, enhanced_image)

# Display each color image with its histogram and save them separately
display_image_with_histogram(original_image, 'Original Image', cv2.calcHist([original_image], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/original_image_with_histogram1.jpg')

display_image_with_histogram(blurred_image, 'Blurred Image',
                              cv2.calcHist([blurred_image], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/blurred_image_with_histogram1.jpg')

display_image_with_histogram(edges, 'Edges on Original Image',
                              cv2.calcHist([edges], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/edges_with_histogram1.jpg')

display_image_with_histogram(cv2.imread(compressed_image_path), 'Compressed Image',
                              cv2.calcHist([cv2.imread(compressed_image_path)], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/compressed_image_with_histogram1.jpg')

display_image_with_histogram(enhanced_image, 'Enhanced Image',
                              cv2.calcHist([enhanced_image], [0], None, [256], [0, 256]),
                              save_path='/mnt/6EAA986CAA983297/python/processedImages/enhanced_image_with_histogram1.jpg')

# Create a final combined image with all images and histograms
fig, axs = plt.subplots(2, 4, figsize=(20, 10))

# Display original image and histogram
axs[0, 0].imshow(original_image)
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')
axs[0, 1].plot(cv2.calcHist([original_image], [0], None, [256], [0, 256]), color='black', linewidth=2)
axs[0, 1].set_title('Histogram - Original Image')
axs[0, 1].set_xlim([0, 256])
axs[0, 1].set_ylim([0, 5000])
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

# Display edges image and histogram
axs[0, 2].imshow(edges, cmap='gray')
axs[0, 2].set_title('Edges')
axs[0, 2].axis('off')
axs[0, 3].plot(cv2.calcHist([edges], [0], None, [256], [0, 256]), color='black', linewidth=2)
axs[0, 3].set_title('Histogram - Edges')
axs[0, 3].set_xlim([0, 256])
axs[0, 3].set_ylim([0, 5000])
axs[0, 3].grid(True, linestyle='--', alpha=0.7)

# Display compressed image and histogram
compressed_image = cv2.imread(compressed_image_path)
axs[1, 0].imshow(compressed_image)
axs[1, 0].set_title('Compressed Image')
axs[1, 0].axis('off')
axs[1, 1].plot(cv2.calcHist([compressed_image], [0], None, [256], [0, 256]), color='black', linewidth=2)
axs[1, 1].set_title('Histogram - Compressed Image')
axs[1, 1].set_xlim([0, 256])
axs[1, 1].set_ylim([0, 5000])
axs[1, 1].grid(True, linestyle='--', alpha=0.7)

# Display enhanced image and histogram
axs[1, 2].imshow(enhanced_image)
axs[1, 2].set_title('Enhanced Image')
axs[1, 2].axis('off')
axs[1, 3].plot(cv2.calcHist([enhanced_image], [0], None, [256], [0, 256]), color='black', linewidth=2)
axs[1, 3].set_title('Histogram - Enhanced Image')
axs[1, 3].set_xlim([0, 256])
axs[1, 3].set_ylim([0, 5000])
axs[1, 3].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('/mnt/6EAA986CAA983297/python/processedImages/final_combined_image.jpg')
plt.show()
