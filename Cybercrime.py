#Import the excel file 
import pandas as pd 
cybercimedata=pd.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Dataanalytic\\Cybercrime.xlsx')
#print(cybercimedata)


#Import the txt file 
file=open('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Dataanalytic\\Message.txt')
userdata=file.read()
#print(userdata)

cybercimeword=cybercimedata['Suspicious word']
Cybercrimeword=list(cybercimeword)
print(Cybercrimeword)


userdata=userdata.split()
userdata=list(userdata)
print(userdata)

#count the number of total word 
tw=len(userdata)
print(tw)

#Logic to find suspicious words
s=0
for eachdata in userdata:
    for eachcybercrimedata in cybercimeword:
        if eachdata.lower()==eachcybercrimedata.lower():
            s=s+1
print(s)
    
ns=tw-s
print(ns)

#Desinge the Pictorial representation
import matplotlib.pyplot as plt
import random 


x=[]
y=[]
for i in range(ns):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))
sx=[]
sy=[]
for i in range(s):
    sx.append(random.randint(1, 10))
    sy.append(random.randint(1, 10))
    
plt.scatter(x, y,color='blue')
plt.scatter(sx, sy,color='red')
plt.show()