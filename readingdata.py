# For extra dependency we need to import the package. 
import pandas 
# Read the data from the excel file
def student(name,marks):
    selectedstudents=list()
    n=len(name)
    for i in range(n):
        if marks[i]>=70:
            selectedname=name[i]
            selectedstudents.append(selectedname)
    return(selectedstudents)

data=pandas.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Dataanalytic\\studentdatabase.xlsx')
#print(data)
#Apply filter to data 
name=data['name']
name=list(name)
print(name)
father=data['father']
#print(father) 
marks=data['marks']
marks=list(marks)
print(marks)
result=student(name,marks)
print(result)


