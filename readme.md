# Python Command-Line Tools

A collection of small yet powerful Python command-line tools designed to help with everyday tasks and automation. This repository includes various utilities that perform functions like image conversion, file handling, data processing, and more.

## Tools Overview

Below are some of the tools currently available in this repository:

1. **ASCII Art Generator**
   - Converts images into ASCII art.
   - Usage:
     ```bash
     python art.py <image_path> -o <output_file>
     ```
   - Example:
     ```bash
     python art.py 'c:/path/to/image.png' -o ascii_art
     ```

2. **MRKDOWN TO HTML CONVERTER**
   - Basically Converts MARKDOWN language content into HTML content. 
   - Usage:
     ```bash
     python mrkdown.py <file_path> -o <OUTPUT> 
     ```
    - Example:
     ```bash
     python art.py 'c:/path/to/readme.md' -o output.html
     ```

3. **File Search**
   - Description of the tool's purpose.
   - Usage:
     ```bash
     python file_search.py </path/to/directory> --name <myfile> --type <txt> --min-size 1000 --max-size 5000 --modified-after 2023-01-01 --modified-before 2023-12-31
     ```

## Getting Started

### Prerequisites
- **Python 3.6+** is required to run these tools.
- Install dependencies by running:
  ```bash
  pip install -r requirements.txt
