
import requests
import csv
from bs4 import BeautifulSoup
address='http://www.teletalk.com.bd/packages/packageDetails.jsp?packageID=3016&menuItem=19005'

page = requests.get(address,verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
for item in list(soup.find_all('table')):
    x=item.find_all('tr')
    print(x.get_text())

#print(soup)