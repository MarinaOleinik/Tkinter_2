from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Teitsmes","Kaheksas"]

def funktion(a):
    tabs.select(a)

def open_():
    file=askopenfilename() #название файла
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

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
def image_phone(name):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(4)
    can.create_image(10,10,image=img,anchor=NW)
root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")
tabs=ttk.Notebook(root)
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Teitsmes","Kaheksas"]
#for i in range(8): #len(texts)
#    tab=Frame(tabs)
#    tabs.add(tab,text=texts[i])
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")

can=Canvas(tab2,width=300,height=200,bg="red")
can.pack()

M=Menu(root)
root.config(menu=M)

m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator='Command+V', command=lambda:funktion(0))
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_command(label="Tab3",command=lambda:funktion(2))
m1.add_command(label="Tab4",command=lambda:funktion(3))
m1.add_separator()



m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Green",command=lambda:root.config(bg="green"))
m2.add_command(label="Blue",command=lambda:root.config(bg="blue"))
m2.add_command(label="Violet",command=lambda:root.config(bg="violet"))

m3=Menu(M,tearoff=0)
M.add_cascade(label="Image",menu=m3)
m3.add_command(label="Cat", command=lambda:image_phone("phone.png"))
m3.add_command(label="Dog", command=lambda:image_phone("phone.png"))
m3.add_command(label="Phone", command=lambda:image_phone("phone.png"))
m3.add_command(label="...", command=lambda:image_phone("phone.png"))

btn_open=Button(tab1,text="Open",command=open_)
btn_save=Button(tab1,text="Save",command=save_)
btn_exit=Button(tab1,text="Exit",command=exit_)
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
#Text(tab1,width=40,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

tabs.pack(fill="both")
root.mainloop()