import requests
from bs4 import BeautifulSoup

URL = 'https://yarnsub.com/yarns/cygnet/chunky'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
tablas = soup.find(class_='details')
filas = tablas.find_all('tr')
for fila in filas :
    print(fila.find('th').text.strip().strip(':'), end=';')
    print(fila.find('td').text.strip())

'''
marca = URL.split('/')[-2]
lana = URL.split('/')[-1]
URL = 'https://yarnsub.com/substitutes/'+marca+'/'+lana
page = requests.get(URL)
'''