from PIL import Image
import argparse

def resize_image(input_path, output_path, width=None, height=None):
    with Image.open(input_path) as img:
        original_width, original_height = img.size

        if width and not height:
            height = int((width / original_width) * original_height)
        elif height and not width:
            width = int((height / original_height) * original_width)
        elif not width and not height:
            width, height = original_width, original_height  

        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(output_path)
        print(f"Image resized and saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Resize an image to a specified width and height.")
    parser.add_argument("input_path", help="The path to the input image.")
    parser.add_argument("output_path", help="The path to save the resized image.")
    parser.add_argument("--width", type=int, help="The desired width of the resized image.")
    parser.add_argument("--height", type=int, help="The desired height of the resized image.")

    args = parser.parse_args()

    resize_image(args.input_path, args.output_path, args.width, args.height)

if __name__ == "__main__":
    main()
