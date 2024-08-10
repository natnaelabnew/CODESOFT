import tkinter
from tkinter import *

root = Tk()
root.title("to do list app(CODESOFT)")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_li = []


def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open(
            "C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/task_list.txt ",
            "a",
        ) as taskfile:
            taskfile.write(f"\n{task}")
        task_li.append(task)
        listbox.insert(END, task)


def delete_task():
    global task_li
    task = str(listbox.get(ANCHOR))
    if task in task_li:
        task_li.remove(task)
        with open(
            "C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/task_list.txt",
            "w",
        ) as taskfie:
            for task in task_li:
                taskfie.write(task + "\n")
        listbox.delete(ANCHOR)


def opentaskfile():
    with open(
        "C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/task_list.txt",
        "r",
    ) as taskfile:
        tasks = taskfile.readlines()
    for task in tasks:
        if task != "/n":
            task_li.append(task)
            listbox.insert(END, task)


# icons
icon_images = PhotoImage(
    file="C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/images/task.png"
)
root.iconphoto(False, icon_images)

# top bar
top_image = PhotoImage(
    file="C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/images/topbar.png"
)
Label(root, image=top_image).pack()
dock_image = PhotoImage(
    file="C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/images/dock.png"
)
Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)


note_image = PhotoImage(
    file="C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/images/task.png"
)
Label(root, image=note_image, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="ALL TASKS", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# frame
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)
task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(
    frame,
    text="add",
    font="arial 20 bold",
    width=6,
    bg="green",
    fg="white",
    bd=0,
    command=addTask,
)
button.place(x=300, y=0)

# list_box
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(
    frame1,
    font="arial 12",
    width=40,
    height=16,
    bg="#32405b",
    fg="white",
    cursor="hand2",
    # selectbackground="#5",
)
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)

scrollbar.pack(side=RIGHT, fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
opentaskfile()

# delete
Delete_icon = PhotoImage(
    file="C:/Users/op/Desktop/CODESOFT/python_internship/CODESOFT/TO_DO_LIST_APP/images/delete.png"
)
Button(root, image=Delete_icon, bd=0, command=delete_task).pack(side=BOTTOM, pady=13)

root.mainloop()
