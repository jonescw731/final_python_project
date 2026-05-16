import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.newschoolfreepress.com/')

urls = [
    'https://www.newschoolfreepress.com/2026/02/16/love-lucy-tackling-roommate-tensions/',
    'https://www.newschoolfreepress.com/2025/12/10/love-lucy-balancing-friendships-and-relationships/',
    'https://www.newschoolfreepress.com/2025/11/19/love-lucy-struggling-to-feel-at-home-in-a-new-place/',
]

def scrape():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    for url in urls:
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Scrapping ...{soup.title.string if soup.title else 'Title not found'} | {soup.time.string if soup.time else 'Not found'}")



scrape()


