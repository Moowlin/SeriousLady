from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Koolitused:
    def __init__(self, name, isikukood, lang, course, basic):
        self.name = name
        self.isikukood = isikukood
        self.lang = lang
        self.course = course
        self.basic = basic

    def printInfo(self):
        print("name: ",self.name, "isikukood: ",self.isikukood, "lang: ", self.lang, "course: ", self.course, "basic: ", self.basic)

massiv = []

def create_ob():
    global massiv
    ob = Koolitused(name.get(), isikukood.get(), lang.get(), course.get(), is_has.get())
    massiv.append(ob)
    print(len(massiv))
    print(massiv)





# -------- Окно
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

# -------- Ввод имени и исикукода
name = StringVar()
isikukood = StringVar()

name_label = Label(text="Sisestage nimi ja isikukood:")

name_entry = Entry(textvariable=name)
isikukood_entry = Entry(textvariable=isikukood)

name_label.grid(row=0, column=0, padx=0, sticky="w")
name_entry.grid(row=1, column=0, padx=1, pady=0)
isikukood_entry.grid(row=1, column=1, padx=1, pady=0)

# -------- Выбор языка
header = Label(text="Keel:", padx=1, pady=1)
header.grid(row=2, column=0, sticky=W)
lang = IntVar()

vene_checkbutton = Radiobutton(text="Vene", value=1, variable=lang, padx=20)
vene_checkbutton.grid(row=3, column=0, sticky=W)

eesti_checkbutton = Radiobutton(text="Eesti", value=2, variable=lang, padx=0)
eesti_checkbutton.grid(row=3, column=1, sticky=W)

# -------- Выбор курса
courses = ('Python','Java','AutoCad','SolidWorks')
course = StringVar()
course_label = Label(text="Vali koolitus:")
course_label.grid(row=4, column=0, sticky="w")
combobox = ttk.Combobox(textvariable=course, width=17)
combobox['values'] = courses
combobox['state'] = 'readonly'
combobox.grid(row=4, column=1)

# -------- Есть ли начальные знания
is_has = IntVar()
is_has_basis_knowledge = Checkbutton(text="On olemas algteadmised", variable=is_has, onvalue=1, offvalue=0)
is_has_basis_knowledge.grid(row=5, column=0)

# -------- Кнопка создания объекта

button_lisa = Button(text="Lisa", command=create_ob)
button_lisa.grid(row=6, column=0, sticky="w", padx=5)


root.mainloop()
