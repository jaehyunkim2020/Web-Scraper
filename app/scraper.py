import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

def scrape_and_save(start_url):
    emails = set()
    contacts = set()

    def scrape_page(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            new_emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))
            emails.update(new_emails)

            ## logic to find contact info (e.g., phone numbers)

            for link in soup.find_all('a', href=True):
                full_url = requests.compat.urljoin(url, link['href'])
                if start_url in full_url and full_url not in visited_urls:
                    visited_urls.add(full_url)
                    scrape_page(full_url)
        
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    
    visited_urls = set()
    visited_urls.add(start_url)
    scrape_page(start_url)

    data = {'Emails': list(emails)}
    df = pd.DataFrame(data)

    file_path = os.path.join(os.getcwd(), 'contacts.csv')
    df.to_csv(file_path, index=False)

    return file_path