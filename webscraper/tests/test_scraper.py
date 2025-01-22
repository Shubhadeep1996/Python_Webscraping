import unittest
from webscraper.scrapers.base_scraper import BaseScraper

class TestBaseScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = BaseScraper()

    def test_http_request(self):
        url = "http://example.com"
        response = self.scraper.make_request(url)
        self.assertEqual(response.status_code, 200)

    def test_parse_html(self):
        html_content = "<html><body><h1>Test</h1></body></html>"
        parsed_data = self.scraper.parse_html(html_content)
        self.assertIn("Test", parsed_data)

if __name__ == '__main__':
    unittest.main()