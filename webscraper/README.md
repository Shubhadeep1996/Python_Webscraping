# Web Scraper Application

A Python web scraping application that can extract data from any website.

## Features
- Extract titles, headers, links and paragraphs
- Save data in CSV or JSON format
- Simple command-line interface

## Installation

### From Source
```bash
git clone https://github.com/Shubhadeep1996/Python_Webscraping.git
cd webscraper
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### Build Commands

# Install development requirements
pip install -r requirements-dev.txt

# Build executable
pyinstaller webscraper.spec

# The executable will be in dist/webscraper.exe