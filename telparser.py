import requests
import csv
from bs4 import BeautifulSoup

address = "http://www.teletalk.com.bd/packages/packageDetails.jsp?packageID=3016&menuItem=19005"
page = requests.get(address,verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
#for item in list(soup.find_all('table')):
 #   print(item.get_text())