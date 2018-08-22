import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.lesbonsnumeros.com/loto/resultats/tirages-decembre-2008.htm'
template = 'tirages-{{mois}}-{{annee}}.htm'
tirage = {
    'date': '',
    'numeros': [],
    'chance': 0
}
def initTirage():
    tirage['date'] = ''
    tirage['chance'] = 0
    tirage['numeros'] = []

def extractTable():
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    monthlyTirage = []
    lines = soup.find_all('ul', attrs={'class': 'tirage tirageSmall loto'})
    for line in lines:
        boules = line.find_all('li', attrs={'class': 'boule'})
        chance = line.find('li', attrs={'class': 'chance'})
        tirage['chance'] = chance.text
        tirage['numeros'].append(boules[0].text)
        tirage['numeros'].append(boules[1].text)
        tirage['numeros'].append(boules[2].text)
        tirage['numeros'].append(boules[3].text)
        tirage['numeros'].append(boules[4].text)
        print(tirage)
        monthlyTirage.append(tirage)
        initTirage()
    return monthlyTirage

print(extractTable())



