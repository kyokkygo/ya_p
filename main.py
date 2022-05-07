from bs4 import BeautifulSoup
import requests


def del_ads(urls_list):
    for el in urls_list:
        if 'yabs' in el:
            urls_list.remove(el)
    del urls_list[-1]
    return urls_list


def get_search_res(url):
    headers = {
        'user-agent': '',
        'cookie': ''
    }
    r = requests.get(url, headers=headers)
    return r.text


def get_urls(html):
    soup = BeautifulSoup(html, 'html5lib')
    urls_in_html = soup.find_all('a', {'class': 'organic__url'})
    urls_list = [a.get('href') for a in urls_in_html]
    return del_ads(urls_list)


def main():
    base_url = 'https://yandex.ru/search/?text='
    #add your query
    query_part = ''
    page_part = '&p='

    for i in range(0, 1):
        url = base_url + query_part + page_part + str(i)

        html = get_search_res(url)
        urls_list = get_urls(html)


if __name__ == '__main__':
    main()
