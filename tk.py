import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter import *

root = tk.Tk()
root.title('Search Bar')

label = ttk.Label(root, text='Search Here', )
label.grid(row=0, column=0 )
entry = ttk.Entry(root, width=50)
entry.grid(row=0, column=1)

def callback():
    
    
        webbrowser.open('http://google.com/search?q='+entry.get())
  
 
MyButton = ttk.Button(root, text='Search', command=callback)
MyButton.grid(row=0, column=2)
root.mainloop()