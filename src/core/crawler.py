import requests
from bs4 import BeautifulSoup

def extract_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mandatory: Remove irrelevant sections [cite: 29, 30, 31, 32]
        for tag in soup(["header", "footer", "nav", "aside", "script", "style", "ad"]):
            tag.decompose()

        title = soup.title.string if soup.title else "No Title"
        # Extract meaningful text [cite: 27]
        text = ' '.join(soup.stripped_strings)
        return text, title
    except Exception as e:
        return None, str(e)