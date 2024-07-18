import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

def scrape_and_save(urls):
    emails = set()
    contacts = set()
    visited_urls = set()

    def scrape_page(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find emails on the page
            new_emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))
            emails.update(new_emails)

            # Add logic to find contact info (e.g., phone numbers)
            # contacts.update(...)

            # Find all links on the page and follow them
            for link in soup.find_all('a', href=True):
                full_url = requests.compat.urljoin(url, link['href'])
                # Ensure we are staying within the same domain
                if any(start_url in full_url for start_url in urls) and full_url not in visited_urls:
                    visited_urls.add(full_url)
                    print(f"Visiting: {full_url}")  # Logging the URL being visited
                    scrape_page(full_url)

        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    
    # Start scraping each provided URL
    for start_url in urls:
        visited_urls.add(start_url)
        print(f"Starting with: {start_url}")  # Logging the starting URL
        scrape_page(start_url)

    # Prepare the data for saving
    data = {'Emails': list(emails)}
    df = pd.DataFrame(data)

    # Save the CSV file
    file_path = os.path.join(os.getcwd(), 'contacts.csv')
    df.to_csv(file_path, index=False)

    return file_path
