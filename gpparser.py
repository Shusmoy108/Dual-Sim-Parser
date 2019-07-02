import requests
import os
import csv
from bs4 import BeautifulSoup
def csvmaker(caller,callee,offer,fnf,starttime,endtime,taka):
    fd = open('gpdata.csv', 'a')
    myCsvRow= caller+','+callee+','+offer+','+fnf+','+starttime+','+endtime+','+str(taka)+'\n'
    fd.write(myCsvRow)
    fd.close()
def othersinfo(str,name):
    list=str.split(':')
    data=list[1].split(' ')
    taka=float(data[1])/10
    csvmaker('GP','Others',name,'N\A','0','24',taka)

def fnfinfo(str,name):

    list=str.split(':')
    if(list[1]==' N/A'):
        print("No fnf")
    else:
        dcheck=list[1].split('&')
        if(len(dcheck)>1):
            fnf=dcheck[0].split('(')
            sfnf=fnf[1].split(' ')
            taka=float(sfnf[0])/10
            #print('superfnf taka: '+taka)
            csvmaker('GP', 'GP', name,'Super', '0','24', taka)
            nfnf=dcheck[1].split("(")
            nfnft=nfnf[1].split(' ')
            ntaka=float(nfnft[0])/10
            #print("Normalfnf taka: "+ntaka)
            csvmaker('GP', 'GP', name,'Normal','0', '24', ntaka)
        else:
            fnf=list[1].split('(')
            fnft=fnf[0].split(' ')
            taka=float(fnft[1])/10
            #print('normal taka: '+taka)
            csvmaker('GP', 'GP', name,'Normal','0', '24', taka)


def pulseinfo(str):
    list=str.split(" ")
    pulse=list[3]
    print('pulse: '+pulse)
def gpinfo(str,name):
    gcheck=str.split(',')
    if(len(gcheck)>1):
        for x in gcheck:
            y=x.split(':')
          
            if(y[0]==' GP to GP '):
                var='GP'
            else:
                var='Com'
            ntk = y[1].split(' ')
            taka = float(ntk[1])/10
            #print(var+'gp taka: ' + taka)
            csvmaker('GP', var,name, 'N\A','0', '24', taka)
    else:
        list=str.split(':')
        var='GP'
        ntk=list[1].split(' ')
        taka=float(ntk[1])/10
        #print(var+'staka: '+taka)
        csvmaker('GP', 'GP',name, 'N\A','0', '24', taka)


address="https://www.grameenphone.com/personal/prepaid-postpaid/prepaid-packages"
page = requests.get(address)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
os.remove("gpdata.csv")
#csvmaker('caller','callee','offer','fnf','starttime','endtime','taka')
for item in list(soup.find_all('li', class_='gpc-list-items')):
    GP = item.find_all('div',class_='gp2gp')
    GPO = item.find_all('div', class_='gp2others')
    FNF = item.find_all('div', class_='fnf')
    pulse = item.find_all('div', class_='pulse')
    title = item.find_all('h2', class_='item-title')
    print('simname:'+title[1].get_text())
    gpinfo(GP[0].get_text(),title[1].get_text())
    othersinfo(GPO[0].get_text(),title[1].get_text())
    fnfinfo(FNF[0].get_text(),title[1].get_text())
    pulseinfo(pulse[0].get_text())
with open('document.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))