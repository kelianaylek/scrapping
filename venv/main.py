import requests
import requests_cache
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

page = r'https://leagueoflegends.fandom.com/wiki/List_of_champions'

class Scrapper():
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def getTitle(self):
        title = self.soup.find('h1', class_='page-header__title').text
        return title

    def getDescription(self):
        description = self.soup.find('div', class_='mw-parser-output').find('p').text
        return description

    def getAvailableChampionList(self):
        championsContainer = self.soup.find('table', class_='article-table').find('tbody')
        championsList = championsContainer.find_all('tr', limit=20)
        del championsList[0]
        champions = []

        for champion in championsList:

            data = champion.find_all('td')

            if(data[4].find('span') != None and data[5].find('span') != None):
                name = data[0].find('span', class_='champion-icon').find('a').text
                role = data[1]['data-sort-value']
                releaseDate = data[2].text.replace('\n', '')
                lastChanged = data[3].find('a').text
                blueEssence = data[4].find('span').text
                riotPoints = data[5].find('span').text

                champion = {
                    'name' : name,
                    'role' : role,
                    'releaseDate' : releaseDate,
                    'lastChanged' : lastChanged,
                    'blueEssence' : blueEssence,
                    'riotPoints' : riotPoints
                }

                champions.append(champion)

        return champions

    def getData(self):
        print(self.getTitle())
        print(self.getDescription())
        print(self.getAvailableChampionList())


Scrapper(page).getData()




