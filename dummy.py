import requests

from bs4 import BeautifulSoup
address = 'https://www.banglalink.net/en'
page = requests.get(address,verify=False)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
#csvmaker('caller', 'callee', 'offer', 'fnf', 'starttime', 'endtime', 'taka')
for item in list(soup.find_all('a', class_='package-detail-link')):
     print(item['href'])
     address1=item['href']
