from tkinter import *

root=Tk() #форма/окно
root.title("Tkinter 1") #заголовок
root.geometry("700x200+100+200")

x = int(input("введите колво столбца "))
def do_message():
    for i in range(x):
        name_st = input("введите название столбца ")
        lbl=Label(text=name_st)
        lbl.grid(row=1, column=i)
        #lbl.pack()

        message_nimi=StringVar()
        textentry=Entry(textvariable=message_nimi) #текст связали с переменной message_nimi
        textentry.grid(row=2, column=i)
        
do_message()

root.mainloop()
