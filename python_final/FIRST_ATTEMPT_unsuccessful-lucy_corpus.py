import requests
import beautifulsoup4

requests.get('https://newschoolfreepress.com/')

urls = [
    'https://www.newschoolfreepress.com/2026/02/16/love-lucy-tackling-roommate-tensions/',
    'https://www.newschoolfreepress.com/2025/12/10/love-lucy-balancing-friendships-and-relationships/',
    'https://www.newschoolfreepress.com/2025/11/19/love-lucy-struggling-to-feel-at-home-in-a-new-place/',
]

for url in urls:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    soup = beautifulsoup4(response.text, 'html.parser')

    paragraphs = soup.find.all('p')
    for p in paragraphs:
        article = "\n".join(p.get_text())

    with open("corpus.txt", "a") as f:
        f.write(article)

