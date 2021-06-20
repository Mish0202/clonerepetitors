from get_html import get_html
from get_url_disciplines import get_url_by_discipline
from get_ankets_count_discipline import get_ankets_count_by_discipline

from bs4 import BeautifulSoup
url = 'https://repetitors.info'

headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Firefox/89.0', 'Content-Type': 'text/html',
}

def get_range():
    url_disciplines_list = get_url_by_discipline()
    for url_discipline in url_disciplines_list:
        discipline = url_discipline.split('/')[-1]
        html_d = get_html(f'https://repetitors.info/repetitor/{discipline}/')
        range_d = get_ankets_count_by_discipline()
        range_discipline = int(range_d)/10*8
        return range_discipline
    return False