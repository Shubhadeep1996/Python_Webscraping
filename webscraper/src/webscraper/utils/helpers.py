import pandas as pd
from bs4 import BeautifulSoup

def clean_data(data):
    """Clean scraped data by removing extra whitespace and newlines"""
    if isinstance(data, str):
        return ' '.join(data.strip().split())
    return data

def extract_links(html_content):
    """Extract all links from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def save_to_csv(data, filename):
    """Save data to a CSV file"""
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False