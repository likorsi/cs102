import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """

    news_list = []

    news = parser.find("table", attrs={"class": "itemlist"})
    title = news.find_all('a', attrs={'class': 'storylink'})
    down = news.find_all('td', attrs={'class': 'subtext'})
    up = news.find_all('tr', attrs={'class': 'athing'})
    

    for i in range(0,30):
     
        url = up[i].find('span', attrs={'class': 'sitestr'})
        if url:
            url = url.text
        else:
            url = 'None'

        points = down[i].find('span', attrs={'class': 'score'})
        if points:
            points = points.text
            point = ''
            for n in points:
                if n.isdigit():
                    point += n
        else:
            point = '0'

        author = down[i].find('a', attrs={'class': 'hnuser'})
        if author:
            author = author.text
        else:
            author = 'None'

        comm = ''
        comments = down[i].find_all('a')
        comment = comments[-1].text
        if comment!='hide' and comment!='discuss':
            for k in comment:
                if k.isdigit():
                    comm += k
        else:
            comm = '0'   

        news_list.append({
            'author': author,
            'comments': comm,
            'points': point,
            'title': title[i].text,
            'url': url
            })
        

    return news_list


def get_news(url='https://news.ycombinator.com/newest', n_pages=34):
    """ Collect news from a given web page """
    news = []
    n=31
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        #next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/newest" + '?next=19164394&n={}'.format(n)
        news.extend(news_list)
        n += 30
        n_pages -= 1
    return news

a = get_news()
for i in range(len(a)):
    print(a[i])
    print("\n")