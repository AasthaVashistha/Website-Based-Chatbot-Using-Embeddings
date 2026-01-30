import unittest
from src.core.crawler import extract_content

class TestCrawler(unittest.TestCase):
    def test_valid_url(self):
        url = "https://example.com"
        text, title = extract_content(url)
        self.assertIsNotNone(text)
        self.assertTrue(len(text) > 0)

if __name__ == "__main__":
    unittest.main()
