import argparse
from mrkdown import mrkdownToHTML

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='A simple command-line tool.')
    
    # Add an argument for the name
    parser.add_argument('path', type=str, help='File Path')
    parser.add_argument('-t',"--tool", type=str, help='<Tool Name> mrkdown --> Convert Markdown to HTML Format', required=False,)
    parser.add_argument('-o',"--output", type=str, help='Output Path', required=True,)

    
    # Parse the arguments
    args = parser.parse_args()

    if args.tool == "m2h":
        try:
            mrkdownToHTML(args.path,args.output+".html")
        except:
            print("Unable to read your file.")
    
    else:
        print("Please choose vaiid -t && --tool")

        

if __name__ == '__main__':
    main()

