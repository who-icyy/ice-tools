import markdown

# Sample Markdown text
markdown_text = """
# Hello, World!
This is a sample Markdown to HTML conversion.
- Item 1
- Item 2
- Item 3
"""

# Convert Markdown to HTML
html_output = markdown.markdown(markdown_text)

# Print the HTML output
print(html_output)
