from bs4 import BeautifulSoup
import requests, csv

z = 'Zweihander'

"url = 'https://eldenring.wiki.fextralife.com/' + z"
url = 'https://rankedboost.com/elden-ring/weapons/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser').find_all('div', class_ = 'tier-list-object-name-table-css')

"info = [needed_info.get_text() for needed_info in soup]"

print(soup[0].get_text())

"""
with open('weapons.csv', 'w', newline='') as data:
    for i in range(len(soup)):
        data.write(soup[i].get_text())
        data.write('\n')
"""