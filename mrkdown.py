import markdown


def mrkdownToHTML(path:str,output:str):
    with open(path, 'r',encoding='latin1') as mrkdown:
        content = mrkdown.read()
    results = markdown.markdown(content)
    mrkdown.close()
    html = open(output,"w",encoding='latin1')
    html.write(results)

