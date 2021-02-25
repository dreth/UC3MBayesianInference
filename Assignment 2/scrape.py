from bs4 import BeautifulSoup as bs
import requests

page = requests.get('https://en.wikipedia.org/wiki/Timeline_of_scientific_discoveries').text
page = bs(page)

# get data
years = [str(x) for x in range(1860,1960,1)]
counts = []
for i in years:
    counts.append()