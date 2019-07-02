
import os
import csv
import requests
from bs4 import BeautifulSoup
#address="https://www.banglalink.net/en/personal/packages?tid=6?tid=6?tid=6&tid=6"
#address="https://www.banglalink.net/en/personal/packages/pre-paid/banglalink-play"
#address="https://www.banglalink.net/en/personal/packages/pre-paid/banglalink-desh-hello-package"
def csvmaker(caller,callee,offer,fnf,starttime,endtime,taka):
    fd = open('blinkdata.csv', 'a')
    myCsvRow= caller+','+callee+','+offer+','+fnf+','+starttime+','+endtime+','+taka+'\n'
    fd.write(myCsvRow)
    fd.close()
def banglalink(list,caller,callee,offer,fnf):
    f=0
    time=''
    front=''
    back=''
    print(list)
    for items in list:
        print(items.get_text())
        if (f == 1):
            ntaka = items.get_text().split('p')
            print('taka')
            print(ntaka)
            if(len(ntaka)>1):
                if((ntaka[1]=='/10sec')or(ntaka[1]=='/10 sec')):
                    t= float(ntaka[0])/10
                    taka=str(t)
                else:
                    taka=str(ntaka[0])
            else:
                taka=str(float(items.get_text())/10)


            print('taka:'+taka)
            f = 0
            str1 = ''+ caller+' '+callee+' '+ offer + ' ' +' '+ fnf +' ' +time + ' ' + taka + '\n'
            #print(str1)
            csvmaker(caller,callee,offer,fnf,front,back,taka)
        if (items.get_text()=='24 hours'):
            f=1

            front='0'
            back='24'
            #print(time)
        else:
            str1= items.get_text().split(' ')
            #print(str1)
            #print(len(str1))
            str2=items.get_text().split('-')
            if((len(str2)==2)and(str1[0]!='S-FNF')):
                if(str2[0]=='12am'):
                    front='0'
                    back='16'
                else:
                    back = '0'
                    front = '16'
                f=1
                time='0-4'

            if(len(str1)==5):
                k=0
                l=0
                tr=items.get_text().split(' ')
                front=''
                back=''
                if(len(tr)==5):
                    if(tr[1]=='pm'):
                        ront=12+int(tr[0])
                        front=str(ront)
                        k=1
                    if(tr[1]=='am'):
                        ront=int(tr[0])
                        front = str(ront)
                        k=1
                    if(tr[4]=='pm'):
                        ack=12+int(tr[3])
                        back = str(ack)
                        l=1
                    if(tr[4]=='am'):
                        ack=int(tr[3])
                        back = str(ack)
                        l=1
                    if((k==1)and(l==1)):
                        #print(front)
                        #print(back)
                        time=''+str(front)+'-'+str(back)
                        print(time)
                        f = 1




def parser(address):
    page = requests.get(address,verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    offer = soup.find_all('div', class_='field field-name-title field-type-ds field-label-hidden field-wrapper')
    off=offer[0].get_text()
    #print(off)
    var=1
    fb=0
    ff=0
    fof=0
    fo=0
    for item in list(soup.find_all('tr')):
        #print(item.get_text())
        str1 = item.find_all('td')
        #print(str[0])
        if(fb==1):
            fb=0
            banglalink(str1, 'Banglalink', 'Banglalink', off, 'N\A')
        if (ff == 1):
            ff = 0
            banglalink(str1, 'Banglalink', 'Banglalink', off, 'A')
        if (fof == 1):
            fof = 0
            banglalink(str1, 'Banglalink', 'Others', off, 'A')
        if (fo == 1):
            fo = 0
            banglalink(str1, 'Banglalink', 'Others', off, 'N\A')

        if((str1[0].get_text()=='Banglalink to Banglalink')or(str1[0].get_text()=='Banglalink To Banglalink')):
            ino = str1[0].attrs
            try:
                row = ino['rowspan']
                if (row == '2'):
                    fb = 1
            except KeyError:
                # Key is not present
                pass


            banglalink(str1, 'Banglalink', 'Banglalink', off, 'N\A')
        if ((str1[0].get_text() == 'Banglalink FNF')or(str1[0].get_text()=='Special FNF')or(str1[0].get_text()=='Banglalink to Banglalink FNF')or(str1[0].get_text()=='S-FNF (Banglalink)')or(str1[0].get_text()=='Super FNF')):
            ino = str1[0].attrs
            try:
                row = ino['rowspan']
                if (row == 2):
                    ff = 1
            except KeyError:
                # Key is not present
                pass

            banglalink(str1, 'Banglalink', 'Banglalink', off, 'A')
        if ((str1[0].get_text() == 'Other operator FNF')or(str1[0].get_text()=='Banglalink to Other Operator FNF')or(str1[0].get_text()=='Banglalink and other operator fnf')):
            ino = str1[0].attrs
            try:
                row = ino['rowspan']
                if (row == 2):
                    fof = 1
            except KeyError:
                # Key is not present
                pass

            banglalink(str1, 'Banglalink', 'Others', off, 'A')

        if((str1[0].get_text()=='To other operators')or(str1[0].get_text()=='To Other Operators')or(str1[0].get_text()=='Banglalink to Other Operator')or(str1[0].get_text()=='Banglalink to other operators')):
            ino = str1[0].attrs
            try:
                row = ino['rowspan']
                if (row == 2):
                    fo = 1
            except KeyError:
                # Key is not present
                pass

            banglalink(str1, 'Banglalink', 'Others', off, 'N\A')


address = "https://www.banglalink.net/en/personal/packages?tid=6?tid=6?tid=6&tid=6"
page = requests.get(address,verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
os.remove("blinkdata.csv")
#print(soup)
#csvmaker('caller', 'callee', 'offer', 'fnf', 'starttime', 'endtime', 'taka')
for item in list(soup.find_all('a', class_='package-detail-link')):
     print(item['href'])
     address1=item['href']
     parser(address1)