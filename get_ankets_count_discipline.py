from get_html import get_html
from get_url_disciplines import get_url_by_discipline
from bs4 import BeautifulSoup

headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Firefox/89.0', 'Content-Type': 'text/html',
}

def get_ankets_count_by_discipline():
    url_discipline_list = get_url_by_discipline()
    for i in url_discipline_list:
        link =f'{i}'
        html_discipline = get_html(link)
        table = BeautifulSoup(html_discipline, 'lxml').find('table', class_='ListanketsPaginator')
        if table:
            row = table.find('td', align='center')
            result = int(row.text.split('из')[-1].split('.')[0].strip())
            print(result)
    return result
get_ankets_count_by_discipline()
  


    
   