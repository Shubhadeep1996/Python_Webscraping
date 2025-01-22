# Python Web Scraper

A robust web scraping application built with Python that extracts and exports website data. Built by Shubhadeep Naskar.

## Features

- Extract website content (titles, headers, links, paragraphs)
- Export data to CSV or JSON formats
- User-friendly command line interface
- Error handling and validation
- Cross-platform compatibility

## Technologies Used

- Python 3.6+
- BeautifulSoup4
- Pandas
- Requests
- PyInstaller

## Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/webscraper.git

# Setup virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

## Project Structure

```markdown
webscraper/
├── src/webscraper/
│   ├── config/      # Configuration settings
│   ├── scrapers/    # Scraping modules
│   └── utils/       # Helper functions
├── tests/           # Unit tests
└── main.py         # Entry point
```

# Install development requirements
pip install -r requirements-dev.txt

# Build executable
pyinstaller webscraper.spec

# Setup development environment
pip install -r requirements-dev.txt
pip install -e .

# Run tests
python -m pytest tests/

# Step-by-Step Plan

1. Project Overview
2. Features
3. Technologies Used  
4. Installation & Setup
5. Usage Instructions
6. Build Process
7. Directory Structure
8. Contributing Guidelines
9. License Information

```markdown
# Python Web Scraper

A robust web scraping application built with Python that extracts and exports website data. Built by Shubhadeep Naskar.

## Features

- Extract website content (titles, headers, links, paragraphs)
- Export data to CSV or JSON formats
- User-friendly command line interface
- Error handling and validation
- Cross-platform compatibility

## Technologies Used

- Python 3.6+
- BeautifulSoup4
- Pandas
- Requests
- PyInstaller

## Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/webscraper.git

# Setup virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

## Project Structure
```
webscraper/
├── src/webscraper/
│   ├── config/      # Configuration settings
│   ├── scrapers/    # Scraping modules
│   └── utils/       # Helper functions
├── tests/           # Unit tests
└── main.py         # Entry point
```

## Building Executable

```bash
# Install development requirements
pip install -r requirements-dev.txt

# Build executable
pyinstaller webscraper.spec
```

## Usage

1. Run the application
2. Enter target website URL
3. Review scraped data summary
4. Choose export format (JSON/CSV)

## Development

```bash
# Setup development environment
pip install -r requirements-dev.txt
pip install -e .

# Run tests
python -m pytest tests/
```

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Author

Shubhadeep Naskar

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request
```