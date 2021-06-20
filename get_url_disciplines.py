import requests
from get_html import get_html
from bs4 import BeautifulSoup


headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Firefox/89.0', 'Content-Type': 'text/html',
}
url = 'https://repetitors.info'

# эта функция получает хтмл от урл и проверяет иксепшены
#def get_html(url):
    #try:
        #result  = requests.get(url, headers=headers)
       # result.raise_for_status()
        #return result.text
    #except(requests.RequestException, ValueError):
        #print('Сетевая ошибка')
        #return False

#эта функция берет хтмл с домашней страницы сайта находит там
# список дисциплин - категорий, создает из них список строк
# в конце возвращает список урлов домашних страниц категорий
def get_url_by_discipline():
    html = get_html('https://repetitors.info/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        num_profiles_by_discipline = soup.find('table', id="mSJs").find('table',  class_="SJlst").find_all('td', class_="wnsj")
        num_list = []
        for num in num_profiles_by_discipline:
            a = num.text
            num_list.append(a)
            #print(a)
        discipline_name = soup.find('table', id="mSJs").find('table',  class_="SJlst").find_all('td', class_="wjnm")
        #print(type(discipline_name))
        discipline_name_list = []
        for name in discipline_name:
            b = name.text
            discipline_name_list.append(b)
            #print(b)
        href_discipline = soup.find_all('td', class_="wjnm")
        url_discipline_list = []
        for href in href_discipline:
            #print(href.find('a').get('href'))
            url_discipline = url + href.find('a').get('href')
            url_discipline_list.append(url_discipline)
        #print(url_discipline_list)
        return url_discipline_list
        
    return False

get_url_by_discipline()