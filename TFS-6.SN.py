from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#-------Всплывающее окно при нажатии Добавить
def show_message():
    messagebox.showinfo("Добавление товара", "Данные о товаре добавлены")

#-------Очистка полей при нажатии Очистить
def delete():
    for i in range(clnmq):
        Entry.delete(0,tk.END)


#-------Вывод столбцов в графическом интерфейсе
def do_message():
    name_columns = ['Id', 'Name', 'Price', 'Vendercode', 'Quantity']
    for i in range(clnmq):
        name_st = name_columns[i]
        lbl=Label(text=name_st)
        lbl.grid(row=2, column=i)

        message_nimi=StringVar()
        textentry=Entry(textvariable=message_nimi, width=25) #текст связали с переменной message_nimi
        textentry.grid(row=3, column=i, padx=5)
    
    #----- Кнопка Добавить
        add_button = Button(text="Добавить", command=show_message, fg="#eee", bg="#333", height=1, width=20)
        add_button.grid(row=4, column=0, sticky="w", padx=5, pady=10)

    #----- Кнопка Очистить
        delete_button = Button(text="Очистить", command=delete).grid(row=4, column=1, padx=5, pady=10)
        
#-------Запрос кол-ва столбцов
try:
    clnmq = int(input("Введите количество необходимых столбцов (Id, Name, Price, Vendercode, Quantity):"))
    if clnmq < 3 and clnmq > 5:
        raise Exception("Столбцов должно быть не менее 3 и не более 5")
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
else:
    print("Запуск программы")
#-------Создание окна
    root = Tk()
    root.title("Таблица товаров") #заголовок
    root.geometry("820x500+200+200")
    lbl2=Label(text="Введите данные о товарах:", fg="#eee", bg="#333", height=2, pady=-10)
    lbl2.grid(row=1, column=0, padx=5)
    
    do_message()
    
    root.mainloop()



