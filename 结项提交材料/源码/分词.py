from PIL import Image, ImageOps
import numpy as np
# Load the uploaded image
uploaded_image_path = r"D:\Acatree_Web\图库\钱伟长背景图1.jpg"
uploaded_image = Image.open(uploaded_image_path)

# Calculate the new width for a 16:9 aspect ratio based on the current image height
new_width = int(uploaded_image.size[1] * (16 / 9))

# If the new width is smaller than the current image width, we'll use the current width
if new_width < uploaded_image.size[0]:
    new_width = uploaded_image.size[0]

# Add padding to the left side of the image to create a 16:9 aspect ratio
# We assume the subject of the photo should remain right-aligned
padding_left = new_width - uploaded_image.size[0]
padding_right = 0  # No padding on the right side
padding_top = 0    # No padding on the top
padding_bottom = 0 # No padding on the bottom

# Create a black gradient for the padding
gradient = np.zeros((uploaded_image.size[1], padding_left, 3), dtype=np.uint8)

# Generate gradient (left is black, fading to transparent towards the image)
for x in range(padding_left):
    gradient[:, x, :] = (1 - (x / padding_left)) * 255

# Convert the numpy array with the gradient to an image
gradient_image = Image.fromarray(gradient.astype('uint8'))

# Convert the gradient image to 'RGB' if necessary
if gradient_image.mode != 'RGB':
    gradient_image = gradient_image.convert('RGB')

# Create a new image with the gradient and the original image
new_image = Image.new('RGB', (new_width, uploaded_image.size[1]))
new_image.paste(gradient_image, (0, 0))
new_image.paste(uploaded_image, (padding_left, 0))

# Save the new image with the gradient
new_image_path = '钱伟长.jpg'
new_image.save(new_image_path)

