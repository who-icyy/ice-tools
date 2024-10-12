import argparse
from mrkdown import mrkdownToHTML

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='A simple command-line tool.')
    
    # Add an argument for the name
    parser.add_argument('path', type=str, help='File Path')
    parser.add_argument('-o',"--output", type=str, help='Output Path', required=True,)    
    # Parse the arguments
    args = parser.parse_args()



        

if __name__ == '__main__':
    main()

