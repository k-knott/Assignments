import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('https://enrarchives.sos.mo.gov/enrnet/')

br.select_form("MainContent_cboraces")
br.form.value = 460006719
br.submit(name = "ctl00$MainContent$btnCountyChange")
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table',
    {'class': 'electtable', 'id': "MainContent_dgrdCountyRaceResults"})

for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    
    writer.writerow(data)