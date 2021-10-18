import pandas
data=pandas.read_excel('C:\\Users\\HP Elitebook G6\\Desktop\\Python\\Dataanalytic\\customerdatabase.xlsx')

def customerproblem(data):
    problem=(input("Enter the customer problem:- "))
    #extract the customer name from database 
    cname=data['name ']
    cname=list(cname)
    #print(cname)
    cproblem=data['problem ']
    cproblem=list(cproblem)
    #print(cproblem)
    index=-1
    for i in (cproblem):
        index=index+1
        databaseproblem=cproblem[index]
        if databaseproblem==problem:
            targetcustomer=cname[index]
            print(targetcustomer)
    
print(data)
#return the customer name whose problem are fake item
reasult=customerproblem(data)