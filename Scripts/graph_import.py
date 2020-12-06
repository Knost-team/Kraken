from tkinter import *

bgf = "#512E5F"
bgb = "#17202A"

# window's generals settings
root = Tk()
root.geometry("720x600")
root.minsize(270, 180)
root.config(bg=bgb)
root.title("Kraken")

liste = []
number = 1
name = "zc"
lliste = []


# button mode execute
def b1():
    var = "e"
    entry_mod.delete(0, END)
    entry_mod.insert(0, var)


# button mode open
def b2():
    var = "o"
    entry_mod.delete(0, END)
    entry_mod.insert(0, var)


# button mode write
def b3():
    var = "w"
    entry_mod.delete(0, END)
    entry_mod.insert(0, var)


# button mode write from file
def b4():
    var = "wf"
    entry_mod.delete(0, END)
    entry_mod.insert(0, var)


# button ccn cut
def c1():
    var = "cut"
    entry_ccn.delete(0, END)
    entry_ccn.insert(0, var)


# button ccn copy
def c2():
    var = "copy"
    entry_ccn.delete(0, END)
    entry_ccn.insert(0, var)


# button ce (Content in Entry)
def d1():
    var = "Y"
    entry_ce.delete(0, END)
    entry_ce.insert(0, var)


# button cm (Content in Memory
def e1():
    var = "Y"
    entry_cm.delete(0, END)
    entry_cm.insert(0, var)


# give an indicator to people when they come
def inter_write():
    a = "command name"
    b = "file"
    m = "parameter"
    c = "arg:w3f,wf,w,open_editor"
    d = "arg2:wf,w"
    e = "arg3:ccn,ce2"
    z = "command to display"
    entry_command2.delete(0, END)
    entry_command2.insert(0, a)
    entry_cmd.delete(0, END)
    entry_cmd.insert(0, z)
    entry_parameter.delete(0, END)
    entry_parameter.insert(0, m)
    entry_command.delete(0, END)
    entry_command.insert(0, a)
    entry_file.delete(0, END)
    entry_file.insert(0, b)
    entry_parmameters.delete(0, END)
    entry_parmameters.insert(0, m)
    entry_arg.delete(0, END)
    entry_arg.insert(0, c)
    entry_arg2.delete(0, END)
    entry_arg2.insert(0, d)
    entry_arg3.delete(0, END)
    entry_arg3.insert(0, e)


# get all from every entry in mode "file"
def a1():
    a = entry_command.get()
    b = entry_file.get()
    m = entry_parmameters.get()
    c = entry_mod.get()
    d = entry_ccn.get()
    e = entry_ce.get()
    f = entry_cm.get()
    g = entry_arg.get()
    h = entry_arg2.get()
    i = entry_arg3.get()
    var = "{}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(i, h, g, f, e, d, c, m, b, a)
    main_entry.delete(0, END)
    main_entry.insert(0, var)


# get all from every entry in mode "command"
def a2():
    a = entry_command2.get()
    b = entry_cmd.get()
    c = entry_parameter.get()
    var = "{}**{}**{}".format(c, b, a)
    main_entry2.delete(0, END)
    main_entry2.insert(0, var)


# make a list with content we get on mode "file" and paste on a main entry ( we can see it when
# press button "Add")
def ee():
    e = main_entry.get()
    d = e.split("-")
    f = []
    for element in d:
        f.insert(0, element)
    return f


# make a list with content we get on mode "command" and paste on a main entry ( we can see it when
# press button "Add")
def ee2():
    e = main_entry2.get()
    d = e.split("**")
    f = []
    for element in d:
        f.insert(0, element)
    return f


# write the content of the list in a file named "doc.txt" (to registre the command and action to do )
def starting():
    b = ee()
    with open("doc.txt", "a+") as file:
        for element in b:
            file.write(element + "\n")
        file.close()


# write the content of the list in a file named "doc2.txt" (to registre the command and action to do )
def starting2():
    b = ee2()
    with open("doc2.txt", "a+") as file:
        for element in b:
            file.write(element + "\n")
        file.close()


# execute a1 , ee and starting
def mamain():
    a1()
    ee()
    starting()


# execute a2, ee2 and starting2
def mamain2():
    a2()
    ee2()
    starting2()


def first_pack():
    first_file.pack(pady=20, expand=YES)
    first_ccmd.pack(pady=20, expand=YES)
    second_pack_forget()
    third_pack_forget()


def first_pack_forget():
    first_file.pack_forget()
    first_ccmd.pack_forget()


def second_packe():
    entry_command.pack()
    entry_file.pack(pady=5)
    entry_parmameters.pack()
    entry_mod.pack(pady=40)
    button_execute.pack(pady=5)
    button_open.pack(pady=5)
    button_write.pack(pady=10)
    entry_ccn.pack(pady=50)
    button_copy.pack(pady=5)
    button_cut.pack(pady=10)
    entry_ce.pack(pady=5)
    button_ce.pack(pady=10)
    entry_cm.pack(pady=10)
    button_cm.pack(pady=10)
    entry_arg.pack(pady=7)
    entry_arg2.pack()
    entry_arg3.pack(pady=3)
    main_button.pack(side=BOTTOM)
    main_entry.pack(side=BOTTOM)
    frame_main.pack(expand=YES)
    frame_left.grid(row=0, column=0, sticky=W)
    frame_right.grid(row=0, column=1, sticky=W)
    first_pack_forget()
    third_pack_forget()


def second_pack_forget():
    frame_main.pack_forget()
    entry_command.pack_forget()
    entry_file.pack_forget()
    entry_parmameters.pack_forget()
    entry_arg.pack_forget()
    entry_arg2.pack_forget()
    entry_arg3.pack_forget()
    main_button.pack_forget()
    main_entry.pack_forget()


def third_pack():
    entry_command2.pack(pady=15)
    entry_cmd.pack(pady=15)
    entry_parameter.pack(pady=15)
    main_entry2.pack(pady=15)
    main_button2.pack(pady=15)
    first_pack_forget()
    second_pack_forget()


def third_pack_forget():
    entry_command2.pack_forget()
    entry_cmd.pack_forget()
    entry_parameter.pack_forget()
    main_entry2.pack_forget()
    main_button2.pack_forget()


frame_main = Frame(root, bg=bgb)
frame_right = Frame(frame_main, bg=bgb)
frame_left = Frame(frame_main, bg=bgb)
entry_command = Entry(root, font=("Arial", 10))
entry_file = Entry(root, font=("Arial", 10))
entry_parmameters = Entry(root, font=("Arial", 10))
button_execute = Button(frame_left, text="Execute", font=("Arial", 10), bg=bgf, command=b1)
button_write = Button(frame_left, text="Write", font=("Arial", 10), bg=bgf, command=b4)
button_open = Button(frame_left, text="Open", font=("Arial", 10), bg=bgf, command=b2)
button_copy = Button(frame_left, text="Copy", font=("Arial", 10), bg=bgf, command=c2)
button_cut = Button(frame_left, text="Cut", font=("Arial", 10), bg=bgf, command=c1)
button_ce = Button(frame_left, text="Content in Entry", font=("Arial", 10), bg=bgf, command=d1)
button_cm = Button(frame_left, text="Content in Memory", font=("Arial", 10), bg=bgf, command=e1)
entry_mod = Entry(frame_right, font=("Arial", 10))
entry_ccn = Entry(frame_right, font=("Arial", 10))
entry_ce = Entry(frame_right, font=("Arial", 10))
entry_cm = Entry(frame_right, font=("Arial", 10))
entry_arg = Entry(root, font=("Arial", 10))
entry_arg2 = Entry(root, font=("Arial", 10))
entry_arg3 = Entry(root, font=("Arial", 10))
main_button = Button(root, text="Add", font=("Arial", 20), bg=bgf, command=mamain)
main_entry = Entry(root, font=("Arial", 20))

first_file = Button(root, text="File", font=("Arial", 20), bg=bgf, command=second_packe)
first_ccmd = Button(root, text="Command", font=("Arial", 20), bg=bgf, command=third_pack)

entry_command2 = Entry(root, font=("Arial", 10))
entry_cmd = Entry(root, font=("Arial", 10))
entry_parameter = Entry(root, font=("Arial", 10))
main_entry2 = Entry(root, font=("Arial", 20))
main_button2 = Button(root, text="Add", font=("Arial", 20), bg=bgf, comman=mamain2)

first_pack()
inter_write()

menu_bar = Menu(root)
menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Quit", command=root.quit)
menu_file.add_command(label="Fist step", command=first_pack)
menu_bar.add_cascade(label="Options", menu=menu_file)
root.config(menu=menu_bar)

root.mainloop()
