!pip install requests
!pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Target URL
url = "http://quotes.toscrape.com"

# Send HTTP request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract quotes and authors
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{text}" - {author}')

