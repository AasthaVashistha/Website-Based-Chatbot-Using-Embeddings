import unittest
from src.core.processor import process_text

class TestProcessor(unittest.TestCase):
    def test_chunking(self):
        sample_text = "This is a test string for Humanli assignment."
        # Assignment requirement: configurable chunk size/overlap [cite: 40]
        docs = process_text(sample_text, "https://test.com", "Test", chunk_size=10, chunk_overlap=2)
        self.assertGreater(len(docs), 0)
        self.assertEqual(docs[0].metadata["source"], "https://test.com")

if __name__ == "__main__":
    unittest.main()
