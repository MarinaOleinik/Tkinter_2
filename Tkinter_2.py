from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys, fileinput
from tkinter.messagebox import *
N=8
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Teitsmes","Kaheksas"]

def funktion(a):
    print(a)
    tabs.select(a)
def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)
    #f=open(file,'r',encoding="utf-8-sig")
    #text=f.readlines()
    #salvestamine
    #f.close()


def save_():
    file=asksaveasfile(mode='w',defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")
root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")
tabs=ttk.Notebook(root)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")
#tabs_list=[]
#for i in range(1,N+1):
#    t='tab'+str(i)
#    t=Frame(tabs)
#    tabs_list.append(t)
    
#    tabs.add(t,text=texts[i-1])

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
var_=IntVar()
M.add_cascade(label="Menu1",menu=m1)

m1.add_command(label="Com1",accelerator='Command+V', command=lambda:funktion(0))
m1.add_separator()
m1.add_command(label="Com2",command=lambda:funktion(1))
m1.add_command(label="Com3",command=lambda:funktion(2))
m1.add_command(label="Com4",command=lambda:funktion(3))
m1.add_separator()

m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_command(label="Violet",command=lambda:root.config(bg="violet"))
btn_open=Button(tab1,text="Open",command=open_)
btn_save=Button(tab1,text="Save",command=save_)
btn_exit=Button(tab1,text="Exit",command=exit_)
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)#Text(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

tabs.pack(fill="both")
root.mainloop()