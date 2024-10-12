import argparse
from PIL import Image

# Characters used for ASCII representation (ordered from darkest to lightest)
ASCII_CHARS = "@%#*+=-:. "

# Resize the image while maintaining aspect ratio
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayscale_image(image):
    return image.convert("L")

# Map each pixel to an ASCII character
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    ascii_length = len(ASCII_CHARS)
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel * ascii_length // 256]  # Map to the appropriate ASCII character
    return ascii_str

# Main function to convert image to ASCII
def image_to_ascii(image_path, new_width=100):
    # Open the image file
    image = Image.open(image_path)

    # Resize and convert to grayscale
    image = resize_image(image, new_width)
    grayscale_image = image.convert("L")

    # Convert pixels to ASCII characters
    ascii_str = pixels_to_ascii(grayscale_image)
    img_width = grayscale_image.width

    # Format the ASCII string into lines
    ascii_art = "\n".join([ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width)])

    return ascii_art


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='A simple command-line tool.')
    
    # Add an argument for the name
    parser.add_argument('path', type=str, help='File Path') 
    parser.add_argument("-o","--output" ,type=str, help='Output Path')
    # Parse the arguments
    args = parser.parse_args()
    # Provide the path to your image file
    image_path = args.path
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)
    if args.output:
        with open(f"{args.output}.txt", "w+") as file:
            file.write(ascii_art)

if __name__ == '__main__':
    main()
