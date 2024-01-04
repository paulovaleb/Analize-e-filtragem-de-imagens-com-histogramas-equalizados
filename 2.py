from PIL import Image
import matplotlib.pyplot as plt

def histogram(image):
    width, height = image.size
    pixels = list(image.getdata())
    histogram = [0]*256
    for pixel in pixels:
        histogram[pixel] += 1
    return histogram

def cumulative_histogram(histogram):
    cumulative_histogram = histogram.copy()
    for i in range(1, 256):
        cumulative_histogram[i] += cumulative_histogram[i-1]
    return cumulative_histogram

def normalize(cumulative_histogram, pixel_count):
    return [round((val * 255) / pixel_count) for val in cumulative_histogram]

def equalize_image(image_path, output_path):
    # Load the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    pixel_count = img.size[0] * img.size[1]

    # Calculate the histogram and the CDF
    hist = histogram(img)
    cdf = cumulative_histogram(hist)

    # Normalize the histogram and the CDF
    hist_normalized = normalize(hist, pixel_count)
    cdf_normalized = normalize(cdf, pixel_count)

    # Equalize the histogram
    pixels = list(img.getdata())
    img_eq_array = [cdf_normalized[pixel] for pixel in pixels]

    # Save the equalized image
    img_eq = Image.new('L', img.size)
    img_eq.putdata(img_eq_array)
    img_eq.save(output_path)

    # Plot the histograms and CDF
    plt.figure(figsize=(24, 6))
    plt.subplot(1, 4, 1)
    plt.bar(range(len(hist)), hist)
    plt.title('Original Histogram')

    plt.subplot(1, 4, 2)
    plt.bar(range(len(hist_normalized)), hist_normalized)
    plt.title('Normalized Histogram')

    plt.subplot(1, 4, 3)
    plt.bar(range(len(cdf)), cdf)
    plt.title('Cumulative Histogram')

    plt.subplot(1, 4, 4)
    plt.bar(range(len(cdf_normalized)), cdf_normalized)
    plt.title('Equalized Histogram')
    plt.show()

# Apply the function on the image "einstein.jpg"
equalize_image('einstein.jpg', 'einstein_equalized.jpg')

# Apply the function on the equalized image
equalize_image('einstein_equalized.jpg', 'einstein_equalized_twice.jpg')
