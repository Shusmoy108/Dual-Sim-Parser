import os

import requests
import csv
from bs4 import BeautifulSoup
def csvmaker(caller,callee,offer,fnf,starttime,endtime,taka):
    fd = open('robidata.csv', 'a')
    myCsvRow= caller+','+callee+','+offer+','+fnf+','+starttime+','+endtime+','+str(taka)+'\n'
    fd.write(myCsvRow)
    fd.close()

def otherinfo(str,name):
    fnf=''
    ui = str.split(" ")
    if (ui[1] == 'FnF'):
        fnf = 'FNF'
    list=str.split("(")
    if(len(list)>1):
        data= list[1].split(" ")
        time=data[0]
        if((data[3]=='paisa/10')or(data[3]=='Paisa/')):
            tarif= float(data[2])/10
        else:
            tarif = float(data[2])
    else:
        li=str.split(" ")
        d = li[1].split('p')
        tarif=float(d[0])/10
    #print('time: '+time)
    #print('taka:'+tarif)
    if (fnf == 'FNF'):
        csvmaker('Robi', 'Others', name, 'A', '0', '24', tarif)
    else:
        csvmaker('Robi', 'Others', name, 'N\A', '0', '24', tarif)


def noorinfo(str):
    list=str.split(":")
    data=list[1].split(" ")
    taka=float(data[1])/10
    #print('taka: '+taka)
    csvmaker('Robi', 'Robi', 'Noor', 'N\A', '0','24', taka)
def robiinfo(stri,name):
    fnf=''
    ui=stri.split(" ")
    if(ui[1]=='FnF'):
        fnf='FNF'
        print(fnf)
    list = stri.split("(")
    if(len(list)>1):
        data = list[1].split(" ")
    else:
        data=stri.split(" ")
    if(data[1]=='hours):'):
        time=data[0]
        tarif = float(data[2])/10
        #print('time: '+time)
        #print('taka: '+tarif)
        if(fnf=='FNF'):
            csvmaker('Robi', 'Robi', name, 'A', '0', '24', tarif)
        else:
            csvmaker('Robi', 'Robi', name, 'N\A', '0', '24', tarif)

    else:
        print(data[2])
        if ((data[2] == 'paisa/10')or(data[2]=='Paisa/')):
            taka = float(data[1])/10
            if (fnf == 'FNF'):
                csvmaker('Robi', 'Robi', name, 'A', '0', '24', taka)
            else:
                csvmaker('Robi', 'Robi', name, 'N\A', '0', '24', taka)
            #print('taka: '+taka)
        else:
            x=''
            y=''
            if(data[1]=='PM'):
                x=int(data[0])+12
            if(data[4]=='PM):'):
                y= int(data[3])+12
            if (data[1]== 'AM'):
                if(data[0]== '12'):
                    x= 0
                else:
                     x=int(data[0])
            if(data[4]=='AM):'):
                if(data[3]=='12'):
                    y=24
                else:
                    y = int(data[3])
            time=''+str(x)+'-'+str(y)
            #print('time: '+time)
            if ((data[6] == 'paisa/10')or(data[6]=='Paisa/')):
                taka = float(data[5]) / 10
            else:
                taka=float(data[5])
            if (fnf == 'FNF'):
                csvmaker('Robi', 'Robi', name, 'A', str(x), str(y), taka)
            else:
                csvmaker('Robi', 'Robi', name, 'N\A', str(x), str(y), taka)
            #print('take: '+taka)
def fnfinfo(r,sim):
    d=r.split('p')
    taka=float(d[0])/10
    csvmaker('Robi', 'Robi', sim, 'A', '0', '24', taka)
def parsing(address):
    page = requests.get(address)
    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup)
    for item in list(soup.find_all('div', class_='bounceIn')):
        siminfo=item.find_all('div',class_='share')
        mylist = item.get_text().split("\n")
        #sim= siminfo.split(" ")
        ino=siminfo[0].attrs
        simname = ino['data-url'].split("/")
        sim=simname.pop()
        #print('Simname: '+sim)
        if(sim=='noor-pack'):
            for x in mylist:
                #print(x)
                strt = x.split("-")
                if (strt[0] == 'Noor'):
                    noorinfo(x)
        for x in mylist:
            #print(x)
            strt= x.split("-")
            if(strt[0]=='Robi'):
                inp = x.split(" ")
                if((inp[0]=='Robi-Others')or(inp[0]=='Robi-Others:')):

                    otherinfo(x,sim)
                else:

                    robiinfo(x,sim)
            else:
                strtp=x.split(" ")

                if(strtp[0]=='FNF:'):
                    fnfinfo(strtp[1],sim)
os.remove('robidata.csv')
#csvmaker('caller', 'callee', 'offer', 'fnf', 'starttime', 'endtime', 'taka')
address="https://www.robi.com.bd/packages/prepaid?page=1&lang=eng"
parsing(address)
address="https://www.robi.com.bd/packages/prepaid?page=2&lang=eng"
parsing(address)
address="https://www.robi.com.bd/packages/prepaid?page=3&lang=eng"
parsing(address)
