import requests
from bs4 import BeautifulSoup

file = open('lanas.txt', 'r')
lineas = file.readlines()
bbdd = []
for linea in lineas:
    URL = linea.strip("\n")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tablas = soup.find(class_='details')
    filas = tablas.find_all('tr')
    marca = URL.split('/')[-2]
    lana = URL.split('/')[-1]
    dic = {'marca': marca, 'lana': lana}
    data = str(marca)+','+str(lana)
    for fila in filas :
        dic[fila.find('th').text.strip().strip(':')] = fila.find('td').text.strip()
        #dicc.append({fila.find('th').text.strip().strip(':'):fila.find('td').text.strip()})
        #print(fila.find('th').text.strip().strip(':'), end=';')
        #print(fila.find('td').text.strip())
    bbdd.append(dic)
print(bbdd) 
'''
marca = URL.split('/')[-2]
lana = URL.split('/')[-1]
URL = 'https://yarnsub.com/substitutes/'+marca+'/'+lana
page = requests.get(URL)
'''