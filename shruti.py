import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skimage import data, img_as_float
from scipy.ndimage import gaussian_filter

# Load a sample image (you can replace this with your own image)
image = img_as_float(data.camera())

# Simulate a blurry image using Gaussian filter
blurry_image = gaussian_filter(image, sigma=1)

# Define universe variables (image intensity ranges)
x = np.linspace(0, 1, 100)

# Generate fuzzy membership functions
intensity = fuzz.gaussmf(x, 0.5, 0.1)  # Gaussian membership function for intensity

# Visualize membership functions
plt.figure()
plt.plot(x, intensity, 'b', linewidth=1.5, label='Intensity')
plt.title('Membership Functions')
plt.legend()

# Define fuzzy rules
# Rule 1: If the intensity is low, increase contrast
# Rule 2: If the intensity is high, decrease contrast

# Membership functions for contrast adjustment
contrast_low = fuzz.gaussmf(x, 0.2, 0.1)  # Low contrast
contrast_high = fuzz.gaussmf(x, 0.5, 0.1)  # High contrast

# Apply fuzzy inference to enhance the image
enhanced_image = np.zeros_like(blurry_image)
for i in range(blurry_image.shape[0]):
    for j in range(blurry_image.shape[1]):
        intensity_level = blurry_image[i, j]
        
        # Fuzzification
        intensity_membership = fuzz.interp_membership(x, intensity, intensity_level)
        
        # Apply rules
        rule1 = np.fmin(intensity_membership, contrast_low)
        rule2 = np.fmin(intensity_membership, contrast_high)
        
        # Combine the rules
        aggregated = np.fmax(rule1, rule2)
        
        # Defuzzification (weighted average)
        enhanced_intensity = fuzz.defuzz(x, aggregated, 'centroid')
        enhanced_image[i, j] = enhanced_intensity

# Display the original, blurry, and enhanced images
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(blurry_image, cmap='gray')
plt.title('Blurry Image')

plt.subplot(1, 3, 3)
plt.imshow(enhanced_image, cmap='gray')
plt.title('Enhanced Image')

plt.tight_layout()
plt.show()