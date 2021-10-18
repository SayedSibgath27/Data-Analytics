import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd





#*************************************************



root= tk.Tk() 
  
figure1 = plt.Figure(figsize=(6,5), dpi=100)

ax1 = figure1.add_subplot()

bar1 = FigureCanvasTkAgg(figure1, root)

graph=bar1.get_tk_widget()
graph.pack(side=tk.LEFT, fill=tk.BOTH)



#******************************************************

data = pd.read_csv("C:\\Users\\HP Elitebook G6\\Downloads\\states.csv",index_col="State")



 
#print(data)
state = data.loc["Kerala"]
#print(state)



confirm=data.loc["Kerala"]["Confirmed"]

confirm_data= list(confirm)

#print(confirm_data)


date=data.loc["Kerala"]["Date"]
date_data= list(date)
#print(date_data)



recover=data.loc["Kerala"]["Recovered"]
print(recover)
recover_data= list(recover)
#print(recover_data)

death=data.loc["Kerala"]["Deceased"]
death_data= list(death)





df = pd.DataFrame({'date':date_data, 'confirm':confirm_data,'recover' :recover_data,'death':death})
df.plot.bar(x='date', y='confirm' ,color='red',legend=True, ax=ax1)
df.plot.bar(x='date', y='recover' ,color='green',legend=True, ax=ax1)
df.plot.bar(x='date', y='death' ,color='blue',legend=True, ax=ax1)




root.mainloop()