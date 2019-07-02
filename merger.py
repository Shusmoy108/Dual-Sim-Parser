import os

os.remove("out.csv")

fout=open("out.csv","a")
myCsvRow = 'caller' + ',' + 'callee' + ',' + 'offer' + ',' + 'fnf' + ',' + 'starttime' + ',' + 'endtime' + ',' + 'taka' + '\n'
fout.write(myCsvRow)
for line in open("gpdata.csv"):
    fout.write(line)
for line in open("robidata.csv"):
    fout.write(line)
for line in open("blinkdata.csv"):
    fout.write(line)
fout.close()