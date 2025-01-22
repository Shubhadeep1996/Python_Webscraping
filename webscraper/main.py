import sys
from src.webscraper.scrapers.base_scraper import BaseScraper
from src.webscraper.utils.helpers import save_to_csv
import json

def validate_url(url):
    return url.startswith(('http://', 'https://'))

def main():
    print("Web Scraper Application")
    print("-" * 50)
    
    # Get URL from user
    url = input("Enter the website URL to scrape: ").strip()
    
    if not validate_url(url):
        print("Error: Please enter a valid URL starting with http:// or https://")
        sys.exit(1)
    
    try:
        # Initialize and run scraper
        print(f"\nScraping {url}...")
        scraper = BaseScraper(url)
        data = scraper.scrape()
        
        if data:
            # Display summary
            print("\nScraping Summary:")
            print(f"Title: {data['title']}")
            print(f"Number of headers: {len(data['headers'])}")
            print(f"Number of links: {len(data['links'])}")
            print(f"Number of paragraphs: {len(data['paragraphs'])}")
            
            # Save options
            save_option = input("\nWould you like to save the data? (json/csv/no): ").lower()
            
            if save_option == 'json':
                with open('scraped_data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
                print("Data saved to scraped_data.json")
            
            elif save_option == 'csv':
                # Convert data to a format suitable for CSV
                flat_data = {
                    'type': [],
                    'content': []
                }
                for key, values in data.items():
                    if isinstance(values, list):
                        for value in values:
                            flat_data['type'].append(key)
                            flat_data['content'].append(value)
                    else:
                        flat_data['type'].append(key)
                        flat_data['content'].append(values)
                
                save_to_csv(flat_data, 'scraped_data.csv')
                print("Data saved to scraped_data.csv")
        
        else:
            print("No data was scraped. Please check the URL and try again.")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()