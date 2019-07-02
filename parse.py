import requests
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
from bs4 import BeautifulSoup
def otherinfo(str):
    ui = str.split(" ")
    if (ui[1] == 'FnF'):
        fnf = 'FNF'
        print(fnf)
    list=str.split("(")
    data= list[1].split(" ")
    time=data[0]
    tarif= data[2]
    print(time)
    print(tarif)
def robiinfo(stri):
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
        print(data[1])
        time=data[0]
        tarif = data[2]
        print(time)
        print(tarif)

    else:
        if (data[2] == 'paisa/10'):
            taka = data[1]
            print(taka)
        else:
            print(data[1] )
            x=0
            y=0
            if(data[1]=='PM'):
                print(data[1])
                x=int(data[0])+12
                print(x)
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
            print(time)
            taka=data[5]
            print(taka)
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
        print(simname.pop())
        for x in mylist:
            #print(x)
            strt= x.split("-")
            if(strt[0]=='Robi'):
                inp = x.split(" ")
                if(inp[0]=='Robi-Others'):
                    print(x)
                    otherinfo(x)
                else:
                    print(x)
                    robiinfo(x)


address="https://www.robi.com.bd/packages/prepaid?page=2&lang=eng#XHjJgHCzfJ8kdqZA.97"
parsing(address)
address="https://www.robi.com.bd/packages/prepaid?page=3&lang=eng#bmYzPFYR4AJukDBZ.97"
parsing(address)
address="https://www.robi.com.bd/packages/prepaid?page=1&lang=eng#BdSr6B7HlBw1Z5VH.97"
parsing(address)
