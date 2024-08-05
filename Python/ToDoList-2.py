#1.A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack()
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    
    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty")
        else:
            messagebox.showwarning("Warning", "No task selected")
    
    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")
    
    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()