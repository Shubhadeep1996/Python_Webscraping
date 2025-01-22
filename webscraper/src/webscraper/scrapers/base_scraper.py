import requests
from bs4 import BeautifulSoup
from ..config.settings import SCRAPING_PARAMS
from ..utils.helpers import clean_data, save_to_csv

class BaseScraper:
    def __init__(self, url):
        self.url = url
        self.headers = SCRAPING_PARAMS['headers']
        self.timeout = SCRAPING_PARAMS['timeout']

    def fetch(self):
        try:
            response = requests.get(
                self.url, 
                headers=self.headers, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None

    def parse(self, html):
        if not html:
            return None
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def extract_data(self, soup):
        if not soup:
            return None
        
        data = {
            'title': soup.title.string if soup.title else '',
            'headers': [h.text for h in soup.find_all(['h1', 'h2', 'h3'])],
            'links': [a.get('href') for a in soup.find_all('a', href=True)],
            'paragraphs': [p.text for p in soup.find_all('p')]
        }
        return data

    def scrape(self):
        html = self.fetch()
        soup = self.parse(html)
        data = self.extract_data(soup)
        return data