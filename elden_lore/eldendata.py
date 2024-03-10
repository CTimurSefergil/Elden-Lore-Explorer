from bs4 import BeautifulSoup
import requests, csv

#Code for getting descriptions from items#
"""
urlItem = 'https://rankedboost.com/elden-ring/weapons/'
pageItem = requests.get(urlItem)
soupItem = BeautifulSoup(pageItem.text, 'html.parser').find_all('div', class_ = 'tier-list-object-name-table-css')[::2]

for i in range(len(soupItem)):
    urlDescription = 'https://eldenring.wiki.fextralife.com/' + soupItem[i].get_text().strip()
    print(urlDescription)
    pageDescription = requests.get(urlDescription)
    soupDescription = BeautifulSoup(pageDescription.text, 'html.parser').find_all('em')

    with open('eldendata.csv', 'a+', newline='') as data:
        data.write('\n')
        for i in range(len(soupDescription)):
            if soupDescription[i].get_text() != 'Int':
                data.write(soupDescription[i].get_text())
                data.write('\n')

"""
"""
#Code for getting item names#

url = 'https://rankedboost.com/elden-ring/weapons/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser').find_all('div', class_ = 'tier-list-object-name-table-css')[::2]

with open('weapons.csv', 'w', newline='') as data:
    for i in range(len(soup)):
        data.write(soup[i].get_text())
        data.write('\n')
        
"""