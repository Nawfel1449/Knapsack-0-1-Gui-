from tkinter import Scale, Tk, Frame, Label, Button ,IntVar,PhotoImage
from tkinter.ttk import Notebook, Entry
from main import knapSack
import PIL 
from PIL import ImageTk, Image
'''
_BACKGROUNDCOLOR = "#c3fdff"
_BACKGROUNDCOLOR_VARIANT = '#5adbee'
'''
_BACKGROUNDCOLOR = "#ECD3CB"
_BACKGROUNDCOLOR_VARIANT = "#a5938e"

window = Tk()
window.title("Knapsack 0/1 solver")
window.geometry("1280x720")
window["bg"] = _BACKGROUNDCOLOR

title = Label(window ,text="Knapsack 0/1 solver")
title.config(font=('Arial' , 27))
title["bg"] = _BACKGROUNDCOLOR
title.pack(padx = 20, pady = 20)


img = ImageTk.PhotoImage(Image.open("logo.png"))
logo = Label(window, image = img)
logo["bg"] = _BACKGROUNDCOLOR
logo.pack(fill = "both")


image_container = Frame(window)

sack_image = ImageTk.PhotoImage(Image.open("sackR.png"))
sack = Label(image_container, image = sack_image)
sack["bg"] = _BACKGROUNDCOLOR
sack.pack(side='left',padx = 180)

element_iamge = ImageTk.PhotoImage(Image.open("elementR.png"))
element = Label(image_container, image = element_iamge)
element["bg"] = _BACKGROUNDCOLOR
element.pack(side = 'right', padx = 70)

image_container["bg"] = _BACKGROUNDCOLOR
image_container.pack(fill="both")


container = Frame(window, borderwidth=1)
container["bg"] = _BACKGROUNDCOLOR

nomber_of_element_entry = Entry(container)
nomber_of_element_entry.pack(side="right", padx=20, pady=10)
nomber_of_element_label = Label(container, text = "Nombre d\'élements : ")
nomber_of_element_label.pack(side="right" ,padx=10, pady=10)
nomber_of_element_label['bg'] = _BACKGROUNDCOLOR

box_wight_label = Label(container , text="Poid du sack : ")
box_wight_label['bg'] = _BACKGROUNDCOLOR
box_wight_label.pack(side="left",padx=5 , pady = 5)
box_wight_entry = Entry(container)
box_wight_entry.pack(side="left",padx=5 , pady = 5)


container.pack(fill="both")

def get_values():
    wt = list()
    val = list()
    n = int(nomber_of_element_entry.get())
    wight = int(box_wight_entry.get())
    for i in range(n):
        wt.append(int(tab1.grid_slaves(1, i+1)[0].get()))
        val.append(int(tab1.grid_slaves(2, i+1)[0].get()))
    val, elem = knapSack(wight, wt, val)
    result = "La gain maximal est de : " + str(val) + "\n" + "La suite des éléments est : " + str(elem)
    lab = Label(frame2,text=result)
    lab.config(font=('Arial' , 22))
    lab["bg"] = _BACKGROUNDCOLOR
    lab.pack(padx = 20, pady = 20)

def reset_table():
    for widget in frame2.winfo_children():
       widget.destroy()
    frame2.pack_forget()
    
def print_table():
    global tab1
    n = int(nomber_of_element_entry.get())
    global frame2
    frame2 = Frame(window)
    frame2['bg'] = _BACKGROUNDCOLOR
    frame2.pack(fill="both")
    tablayout = Notebook(frame2)
    tab1 = Frame(tablayout)
    tab1['bg'] = _BACKGROUNDCOLOR
    tab1.pack(fill="both")

    for row in range(3):
        for column in range(n + 1):
            if column == 0:
                if row == 1:
                    label = Label(tab1, text="Poid")
                    label.config(font=('Arial', 14))
                    label['bg']=_BACKGROUNDCOLOR_VARIANT
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)
                elif row == 2:
                    label = Label(tab1, text="Valeur")
                    label.config(font=('Arial', 14))
                    label['bg']=_BACKGROUNDCOLOR_VARIANT
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)
            else:
                if row == 0:
                    label = Label(tab1, text="Element : " + str(column))
                    label.config(font=('Arial', 14))
                    label['bg']=_BACKGROUNDCOLOR_VARIANT
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)
                else:
                    label = Entry(tab1, text="Row : " + str(row) + " , Column : " + str(column))
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    tab1.grid_columnconfigure(column, weight=1)

    tablayout.pack(fill="both")
    calc = Button(frame2, text="calculat", command =get_values)
    calc.pack(padx = 20, pady = 20)

    reset = Button(frame2, text = "Reset" , command = reset_table)
    reset.pack(padx = 5, pady = 5)


    return tab1


button = Button(window, text="Ajouter des èlements", command=print_table)
button.pack()



window.mainloop()