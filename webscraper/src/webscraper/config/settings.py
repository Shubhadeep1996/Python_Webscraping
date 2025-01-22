# File: /webscraper/webscraper/src/webscraper/config/settings.py

# Configuration settings for the web scraping application

BASE_URL = "https://example.com"  # Replace with the target website
SCRAPING_PARAMS = {
    "timeout": 10,
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
}