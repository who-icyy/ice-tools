import argparse
import markdown


def mrkdownToHTML(path:str,output:str):
    with open(path, 'r',encoding='latin1') as mrkdown:
        content = mrkdown.read()
    results = markdown.markdown(content)
    mrkdown.close()
    html = open(output,"w",encoding='latin1')
    html.write(results)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='A markdown to html converter')
    
    # Add an argument for the name
    parser.add_argument('path', type=str, help='File Path')
    parser.add_argument('-o',"--output", type=str, help='Output Path', required=True,)    
    # Parse the arguments
    args = parser.parse_args()

    
    try:
        mrkdownToHTML(args.path,args.output+".html")
    except:
        print("Unable to read your file.")


if __name__ == '__main__':
    main()

