# import numpy as np
# import matplotlib.pyplot as plt
# import skfuzzy as fuzz
# from skimage import data, img_as_float
# from scipy.ndimage import gaussian_filter

# # Load a sample image (you can replace this with your own image)
# image = img_as_float(data.camera())

# # Simulate a blurry image using Gaussian filter
# blurry_image = gaussian_filter(image, sigma=1)

# # Define universe variables (image intensity ranges)
# x = np.linspace(0, 1, 100)

# # Generate fuzzy membership functions
# intensity = fuzz.gaussmf(x, 0.5, 0.1)  # Gaussian membership function for intensity

# # Visualize membership functions
# plt.figure()
# plt.plot(x, intensity, 'b', linewidth=1.5, label='Intensity')
# plt.title('Membership Functions')
# plt.legend()

# # Define fuzzy rules
# # Rule 1: If the intensity is very low, increase contrast significantly
# # Rule 2: If the intensity is low, increase contrast moderately
# # Rule 3: If the intensity is high, decrease contrast moderately
# # Rule 4: If the intensity is very high, decrease contrast significantly

# # Membership functions for contrast adjustment
# contrast_very_low = fuzz.gaussmf(x, 0.1, 0.1)  # Very low contrast
# contrast_moderate_low = fuzz.gaussmf(x, 0.3, 0.1)  # Moderate low contrast
# contrast_moderate_high = fuzz.gaussmf(x, 0.7, 0.1)  # Moderate high contrast
# contrast_very_high = fuzz.gaussmf(x, 0.8, 0.1)  # Very high contrast

# # Apply fuzzy inference to enhance the image
# enhanced_image = np.zeros_like(blurry_image)
# for i in range(blurry_image.shape[0]):
#     for j in range(blurry_image.shape[1]):
#         intensity_level = blurry_image[i, j]
        
#         # Fuzzification
#         intensity_membership = fuzz.interp_membership(x, intensity, intensity_level)
        
#         # Apply rules
#         rule1 = np.fmin(intensity_membership, contrast_very_low)
#         rule2 = np.fmin(intensity_membership, contrast_moderate_low)
#         rule3 = np.fmin(intensity_membership, contrast_moderate_high)
#         rule4 = np.fmin(intensity_membership, contrast_very_high)
        
#         # Combine the rules
#         aggregated = np.fmax.reduce([rule1, rule2, rule3, rule4])
        
#         # Defuzzification (weighted average)
#         enhanced_intensity = fuzz.defuzz(x, aggregated, 'centroid')
#         enhanced_image[i, j] = enhanced_intensity

# # Display the original, blurry, and enhanced images
# plt.figure(figsize=(15, 4))

# plt.subplot(1, 4, 1)
# plt.imshow(image, cmap='gray')
# plt.title('Original Image')

# plt.subplot(1, 4, 2)
# plt.imshow(blurry_image, cmap='gray')
# plt.title('Blurry Image')

# plt.subplot(1, 4, 3)
# plt.imshow(enhanced_image, cmap='gray')
# plt.title('Enhanced Image')

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skimage import data, img_as_float
from scipy.ndimage import gaussian_filter

# Load a sample image (you can replace this with your own image)
image = img_as_float(data.camera())

# Simulate a blurry image using Gaussian filter
blur_sigma = float(input("Enter the blur level (e.g., 1.0): "))
blurry_image = gaussian_filter(image, sigma=blur_sigma)

# Define universe variables (image intensity ranges)
x = np.linspace(0, 1, 100)

# Generate fuzzy membership functions
intensity_mean = float(input("Enter the average intensity value (e.g., 0.5): "))
intensity_sigma = float(input("Enter the intensity spread (e.g., 0.1): "))
intensity = fuzz.gaussmf(x, intensity_mean, intensity_sigma)

# Membership functions for contrast adjustment
contrast_means = float(input("Enter the average contrast value (e.g., 0.5): "))
contrast_sigma = float(input("Enter the contrast spread (e.g., 0.1): "))
contrast_very_low = fuzz.gaussmf(x, contrast_means - 0.2, contrast_sigma)
contrast_moderate_low = fuzz.gaussmf(x, contrast_means - 0.1, contrast_sigma)
contrast_moderate_high = fuzz.gaussmf(x, contrast_means + 0.1, contrast_sigma)
contrast_very_high = fuzz.gaussmf(x, contrast_means + 0.2, contrast_sigma)

# Plot fuzzy membership functions
plt.figure(figsize=(8, 6))

plt.plot(x, intensity, 'b', linewidth=1.5, label='Intensity')
plt.plot(x, contrast_very_low, 'r', linewidth=1.5, label='Contrast Very Low')
plt.plot(x, contrast_moderate_low, 'g', linewidth=1.5, label='Contrast Moderate Low')
plt.plot(x, contrast_moderate_high, 'c', linewidth=1.5, label='Contrast Moderate High')
plt.plot(x, contrast_very_high, 'm', linewidth=1.5, label='Contrast Very High')

plt.title('Fuzzy Membership Functions')
plt.xlabel('Intensity')
plt.ylabel('Membership Value')
plt.legend()
plt.grid(True)
plt.show()

# Apply fuzzy inference to enhance the image
enhanced_image = np.zeros_like(blurry_image)
for i in range(blurry_image.shape[0]):
    for j in range(blurry_image.shape[1]):
        intensity_level = blurry_image[i, j]

        # Fuzzification
        intensity_membership = fuzz.interp_membership(x, intensity, intensity_level)

        # Apply rules
        rule1 = np.fmin(intensity_membership, contrast_very_low)
        rule2 = np.fmin(intensity_membership, contrast_moderate_low)
        rule3 = np.fmin(intensity_membership, contrast_moderate_high)
        rule4 = np.fmin(intensity_membership, contrast_very_high)

        # Combine the rules
        aggregated = np.fmax.reduce([rule1, rule2, rule3, rule4])

        # Defuzzification (weighted average)
        enhanced_intensity = fuzz.defuzz(x, aggregated, 'centroid')
        enhanced_image[i, j] = enhanced_intensity

# Display the original, blurry, and enhanced images
plt.figure(figsize=(15, 4))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 4, 2)
plt.imshow(blurry_image, cmap='gray')
plt.title('Blurry Image')

plt.subplot(1, 4, 3)
plt.imshow(enhanced_image, cmap='gray')
plt.title('Enhanced Image')

plt.tight_layout()
plt.show()