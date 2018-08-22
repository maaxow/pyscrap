import urllib.request
import json
from bs4 import BeautifulSoup

#url = 'https://www.lesbonsnumeros.com/loto/resultats/tirages-janvier-2009.htm'
url = 'http://www.tirage-euromillions.net/loto/annee/tirages-2008/'
template = 'tirages-{mois}-{annee}.htm'
#print(template.format(mois='decembre', annee='2008'))
tirage = {
    'date': '',
    'numeros': [],
    'chance': 0
}
f = open('data.json', 'r+')

def extractTable():
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html5lib')
    monthlyTirage = []
    table = soup.find('table', id='tiragesAnneeLoto')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    #file = open('page.html', 'r+')
    #file.write('')
    #file.write(str(trs))
    #file.close()
    #print(str(trs))
    file = open('page.html', 'r+')
    file.write('')
    for line in rows:
        tds = line.find_all('td')
        tirage = {
            'date': '',
            'numeros': [],
            'chance': 0
        }
        if len(tds) == 9:
            date = tds[0].a.text
            tirage['date'] = tds[0].a.text
            file.write(str(date))
            file.write('\n')

        #tirage['chance'] = chance.text
        #tirage['numeros'].append(boules[0].text)
        #tirage['numeros'].append(boules[1].text)
        #tirage['numeros'].append(boules[2].text)
        #tirage['numeros'].append(boules[3].text)
        #tirage['numeros'].append(boules[4].text)
        monthlyTirage.append(tirage)
        
    json.dump(monthlyTirage, f)
    file.close()
    return monthlyTirage

extractTable()
f.close()



