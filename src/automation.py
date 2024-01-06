import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Page has been retrieved")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")