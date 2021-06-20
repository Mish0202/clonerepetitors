import requests

headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Firefox/89.0', 'Content-Type': 'text/html',
}
url = 'https://repetitors.info'

# эта функция получает хтмл от урл и проверяет иксепшены
def get_html(url):
    try:
        result  = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False