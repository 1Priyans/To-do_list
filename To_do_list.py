import tkinter
import random
from tkinter import messagebox

# Create root Window
root = tkinter.Tk()

root.configure(bg="white")

root.title("My To Do List")

# Change the window size
root.geometry("375x275")

tasks = []

tasks = ["Do Exercise", "Buy a book", "Do Coding", "Eat Meal"]

# Create Functions

def update_listbox():
    #Clear the current list
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    task = txt_input.get()# Get the task to add
    # Make sure the task is not empty
    if task != "":
        tasks.append(task)#Append to the list
        update_listbox() # Update the listbox
    else:
        messagebox.showwarning("Warning","You need to enter the text")
    txt_input.delete(0,"end")
def del_all():
    conform_del = messagebox.askyesno("Please Confirm","Do yoy really want to delete all tasks")
    if conform_del == True:
        global tasks #Since we are changing the list it needs to be global
        tasks = [] #Clear the task list
        update_listbox() #Update the listbox


def del_one():
    task = lb_tasks.get("active")#Get the text of the currently selected item
    if task in tasks:#Conform it is in the list
        tasks.remove(task)
    update_listbox()


def sort_asc():
    tasks.sort()
    update_listbox()  # Update the listbox

def sort_desc():
    tasks.sort()
    tasks.reverse() # Reverse the tasks list
    update_listbox()  # Update the listbox

def choose_random():
    task = random.choice(tasks) #Choose the random tasks
    # Update the display label
    lbl_display["text"] = task

def show_number_of_task():
    number_of_task = len(tasks) # Get the number of tasks
    msg = "Number of tasks: %s" %number_of_task # Create and format the message
    lbl_display["text"] = msg # Display the msg


lbl_title = tkinter.Label(root, text="To-Do-List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="",bg="white")
lbl_display.grid(row=0,column=1)


txt_input = tkinter.Entry(root, width=20)
txt_input.grid(row=1,column=1)


btn_add_task= tkinter.Button(root, text="Add task", fg="green", bg="white",command=add_task)
btn_add_task.grid(row=1,column=0)


btn_del_all = tkinter.Button(root, text="Delete All",fg="red",bg="white",command=del_all)
btn_del_all.grid(row=2,column=0)



btn_del_one= tkinter.Button(root, text="Delete One",fg="red",bg="white",command=del_one)
btn_del_one.grid(row=3,column=0)


btn_sort_asc = tkinter.Button(root, text="Sort Ascending",fg="green",bg="white",command=sort_asc)
btn_sort_asc.grid(row=4,column=0)


btn_sort_desc = tkinter.Button(root, text="Sort Descending",fg="green",bg="white",command=sort_desc)
btn_sort_desc.grid(row=5,column=0)


btn_choose_random = tkinter.Button(root, text="Choose Random",fg="green",bg="white",command=choose_random)
btn_choose_random.grid(row=6,column=0)


btn_show_number_of_task = tkinter.Button(root, text="Number of Tasks",fg="green",bg="white",command=show_number_of_task)
btn_show_number_of_task.grid(row=7,column=0)


btn_exit = tkinter.Button(root, text="Exit",fg="green",bg="white",command=exit)
btn_exit.grid(row=8,column=0)


lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

root.mainloop()

