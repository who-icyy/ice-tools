import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='A simple command-line tool.')
    
    # Add an argument for the name
    parser.add_argument('path', type=str, help='File Path')
    parser.add_argument('-o',"--output", type=str, help='File Path', required=True,)

    
    # Parse the arguments
    args = parser.parse_args()

    if args.output : print("out")
    
    # Print the greeting
    print(f"Hello, {args.path}!")

if __name__ == '__main__':
    main()

