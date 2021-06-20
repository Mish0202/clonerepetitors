from get_html import get_html
from get_url_disciplines import get_url_by_discipline
from get_ankets_count_discipline import get_ankets_count_by_discipline
from get_range_discipline import get_range
from bs4 import BeautifulSoup
url = 'https://repetitors.info'

headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Firefox/89.0', 'Content-Type': 'text/html',
}

# по идее при range = 1 я должен получить по 1 репетитору на каждую 
# дисциплину, но получаю только 10 репетиторов
def get_info_ankets():
    url_disciplines_list = get_url_by_discipline()
    for url_discipline in url_disciplines_list:
        discipline = url_discipline.split('/')[-1]
        page = 0
        for i in range(1):
            # должна для 1ой дисциплины в списке пойти на ее первую 
            # страницу и взять первую анкету , цикл закончился
            # должна вернуться к первому  for так как там список из 24 дисциплин
            # и вернуть 24 анкеты 24 репетиторов по разным предметам

            # а возвращает 10 репов  и часть из них по одному предмету - математике
            html = get_html(f'https://repetitors.info/repetitor/{discipline}/?L={page}')
            soup = BeautifulSoup(html, 'lxml')
            allAnkets = soup('table', class_="AnkTB")
            for anketa in allAnkets: # почему то распечатывает только 1ю - математику
                print(url_discipline)
                name = anketa.find('b', class_='pnmst').text
                print(name)
                title = anketa.find_all('p')[1].text
                print(title)
                url_photo_2 = anketa.find('img').get('src')
                url_photo_1 = 'https:'
                url_photo = url_photo_1 + url_photo_2
                print(url_photo)
                url_profile = anketa.find('b', class_='pnmst').find('a').get('href')
                print(url+url_profile)
                prices = anketa.find_all('p')[-4:-1]
                for p in prices:
                    print(p.text)          
        
            #page +=8
    return True
    #return True - return с этой индентацией дает 24 повтора по 10 анкет
    # тех же анкет и в том же порядке, что получены ранее
get_info_ankets()  
