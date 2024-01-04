from PIL import Image
import numpy as np

def normalize(image_array, min_val, max_val):
    return min_val + (max_val - min_val) * (image_array - image_array.min()) / (image_array.max() - image_array.min())

def apply_transformation(image_path, output_path, transformation):
    # Load the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)

    # Apply the transformation
    img_transformed_array = transformation(img_array)

    # Normalize the pixel values to the range 0 to 255 after applying the transformation
    img_transformed_array = normalize(img_transformed_array, 0, 255)

    # Ensure that the pixel values are in the range 0 to 255
    img_transformed_array = np.clip(img_transformed_array, 0, 255).astype(np.uint8)

    # Save the transformed image
    img_transformed = Image.fromarray(img_transformed_array)
    img_transformed.save(output_path)

# Define the transformations
c = 5.0
b = 0.0
transformation_a = lambda f: c * f + b
transformation_b = lambda f: c * np.log2(f + 1)
transformation_c = lambda f: c * np.exp(f / 255.0)

# Apply the transformations to the image "einstein.jpg"
apply_transformation('einstein.jpg', 'einstein_transformed_a.jpg', transformation_a)
apply_transformation('einstein.jpg', 'einstein_transformed_b.jpg', transformation_b)
apply_transformation('einstein.jpg', 'einstein_transformed_c.jpg', transformation_c)
