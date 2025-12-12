from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup

def scrape(sub_red):
    token = 'dLN3qq4_CCZeNJTAPTwGdA'
    reddit_url = 'https://www.reddit.com/r/' + sub_red + '/new/'
    api = CrawlingAPI({'token': token})
    response = api.get(reddit_url)

    if response['status_code'] == 200:
        return response['body']
    else:
        print('Error')

def parse(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    instances = soup.find_all('div', property="schema:articleBody")
    docs = []
    for instance in instances:
        for p_tag in instance:
            if p_tag:
                docs.append(''.join(p_tag.get_text().strip()))
    return docs