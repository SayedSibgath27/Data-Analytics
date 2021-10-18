#Reading a data in txt format
file=open("C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Dataanalytic\\database.txt",'r')
content=file.read()
print(content)
#Apply data Analytic on this file
data=content.split()
print(data)
numberofword=len(data)
print(numberofword)


data1=content.split('\n')
print(data1)
numberofline=len(data1)
print(numberofline)

data2=content.split('\t')
print(data2)

data3=list(content)
print(data3)

numberofletter=len(data3)
print(numberofletter)
print(len(content))