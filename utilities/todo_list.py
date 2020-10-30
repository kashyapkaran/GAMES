import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("to-do List by Karan Kashyap")

def add_task():
    task = entry_task.get()
    listbox_tasks.insert(tkinter.END, task)
    entry_task.delete(0, tkinter.END)



#Gui's
listbox_tasks = tkinter.Listbox(root, height=3, width=50)
listbox_tasks.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()







root.mainloop()