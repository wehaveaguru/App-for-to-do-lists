from tkinter import *

window=Tk()
window.title("To-Do List")
window.minsize(height=200, width=300)
window.config(padx=20, pady=20)

title_label=Label(text="To-Do List", font=("Arial", 24, "bold"))
title_label.grid(row=0, column=1)

task_entry=Entry(width=30)
task_entry.grid(row=1, column=0, columnspan=2)
task_entry.focus()

def add_task():
    task=task_entry.get()
    if task:
        with open("tasks.txt","a") as f:
            f.write(f"{task}\n")
        task_entry.delete(0, END)
add_task_button=Button(text="Add Task", width=15, command=add_task)
add_task_button.grid(row=1,column=2)

window.mainloop()

