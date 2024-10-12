import requests
from bs4 import BeautifulSoup
import argparse

def scrape_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Scrape links from a webpage.")
    parser.add_argument("url", help="The URL of the webpage to scrape.")

    args = parser.parse_args()

    links = scrape_links(args.url)

    if links:
        print("Links found on the page:")
        for link in links:
            print(link)
    else:
        print("No links found or an error occurred.")

if __name__ == "__main__":
    main()
