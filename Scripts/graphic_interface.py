from tkinter import *
from files.class_action import *

bgf = "#512E5F"
bgb = "#17202A"

# window's generals settings
window = Tk()
window.geometry("720x550")
window.minsize(270, 180)
window.config(bg=bgb)
window.title("Kraken")

chox = 0
nb2 = 0
liste2 = []
h = []
nb3 = 1
nb4 = 2
liste = []
hecto = []
maxi = 0
nb = 0
nbb = 1
nbb2 = 2
nbb3 = 3
nbb4 = 4
nbb5 = 5
nbb6 = 6
nbb7 = 7
nbb8 = 8
nbb9 = 9
ttest = []


# execute the action when tipe the command name
def find():
    arg = inpute.get()
    tt = arg.split("**")
    for element in liste:
        if tt[0] == element.get_command():
            if element.get_parameter() == "Y":
                if len(tt) == 2:
                    element.big_one(inpute2, END, this=tt[1], this2=tt[1], this3=tt[1])
                elif len(tt) == 3:
                    element.big_one(inpute2, END, this=tt[1], this2=tt[2], this3=tt[2])
                elif len(tt) == 4:
                    element.big_one(inpute2, END, this=tt[1], this2=tt[2], this3=tt[3])
            else:
                element.big_one(inpute2, END, this=tt[0], this2=tt[0], this3=tt[0])
    for element in liste2:
        if tt[0] == element.get_command():
            if element.get_parameter() == "Y":
                element.todo(tt[1])
            else:
                element.todo(tt[0])


def executelist():
    with open("executelist.txt", "r+") as file:
        arg = file.readlines()
        file.close()
    for line in arg:
        tt = line.split("**")
        for element in liste:
            if tt[0] == element.get_command():
                if element.get_parameter() == "Y":
                    if len(tt) == 2:
                        element.big_one(inpute2, END, this=tt[1], this2=tt[1], this3=tt[1])
                    elif len(tt) == 3:
                        element.big_one(inpute2, END, this=tt[1], this2=tt[2], this3=tt[2])
                    elif len(tt) == 4:
                        element.big_one(inpute2, END, this=tt[1], this2=tt[2], this3=tt[3])
                else:
                    element.big_one(inpute2, END, this=tt[0], this2=tt[0], this3=tt[0])
        for element in liste2:
            if tt[0] == element.get_command():
                if element.get_parameter() == "Y":
                    element.todo(tt[1])
                else:
                    element.todo(tt[0])


# import all the actions when saved in "doc.txt"
# and associate it with an instance of the action object
def read_program():
    global hecto
    global ttest
    global nb, nbb, nbb2, nbb3, nbb4, nbb5, nbb6, nbb6, nbb7, nbb8, nbb9
    global maxi
    with open("doc.txt", "r+") as file:
        hecto = file.readlines()
        maxi = len(hecto)
        file.close()
    while nb < maxi:
        mex = "{}{}{}{}{}{}{}{}{}{}".format(hecto[nb], hecto[nbb], hecto[nbb2], hecto[nbb3], hecto[nbb4], hecto[nbb5],
                                            hecto[nbb6],
                                            hecto[nbb7], hecto[nbb8], hecto[nbb9])
        nb += 10
        meex = mex.split("\n")
        liste.append(Action(meex[0], meex[1], meex[2], meex[3], meex[4], meex[5], meex[6], meex[7], meex[8], meex[9]))
        nbb += 10
        nbb2 += 10
        nbb3 += 10
        nbb4 += 10
        nbb5 += 10
        nbb6 += 10
        nbb7 += 10
        nbb8 += 10
        nbb9 += 10
        for element in liste:
            print(element.get_command())


# import all actions we saved on "doc2.txt"
# and associate it with an instance of the ccmd object
def read_program_ccmd():
    global nb2, nb3, chox, h, liste2, nb4
    with open("doc2.txt", "r+") as file:
        h = file.readlines()
        chox = len(h)
        file.close()
    while nb2 < chox:
        mex = "{}{}{}".format(h[nb2], h[nb3], h[nb4])
        nb2 += 3
        meex = mex.split("\n")
        liste2.append(Ccmd(meex[0], meex[1], meex[2]))
        nb3 += 3
        nb4 += 3
        for element in liste2:
            print(element.get_command())


def mainan():
    read_program()
    read_program_ccmd()
    pack_base()


# window's presentation
# frame centre
frame_centre = Frame(window, bg=bgb)
# canvas + image
width = 128
image = PhotoImage(file="octopus.png").zoom(1).subsample(1)
canvas = Canvas(frame_centre, width=width, height=width, bg=bgb, bd=0, highlightthickness=0)
canvas.create_image(width / 2, width / 2, image=image)
# frame decalee
frame_baquale = Frame(frame_centre, bg=bgb)
inpute = Entry(frame_baquale, font=("Arial", 10))
bouton = Button(frame_baquale, text="Krak", font=("Arial", 10), bg=bgf, command=find)
inpute2 = Entry(frame_baquale, font=("Arial", 15))
button_import = Button(window, text="Import", font=("Arial", 30), bg=bgf, command=mainan)


def pack_base():
    second_pack_forget()
    canvas.grid(row=0, column=0, sticky=W)
    inpute.pack()
    bouton.pack(pady=5)
    inpute2.pack(pady=10)
    frame_baquale.grid(row=0, column=1, sticky=W)
    frame_centre.pack(expand=YES)


def pack_forget_base():
    frame_centre.pack_forget()


def second_pack():
    pack_forget_base()
    button_import.pack(expand=YES)


def second_pack_forget():
    button_import.pack_forget()


menu_bar = Menu(window)
menu_file2 = Menu(menu_bar, tearoff=0)
menu_file2.add_command(label="Quit", command=window.quit)
menu_file2.add_command(label="Test", command=second_pack)
menu_file2.add_command(label="Test2", command=pack_base)
menu_bar.add_cascade(label="File", menu=menu_file2)
window.config(menu=menu_bar)

read_program()
read_program_ccmd()
pack_base()
executelist()
window.mainloop()
