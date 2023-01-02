from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
listbox = ttk.Treeview(root, columns=("listbox", "c2", "c3", "c4"), show="headings")
listbox.column("# 1", anchor=CENTER)
listbox.heading("# 1", text="ID")
listbox.column("# 2", anchor=CENTER)
listbox.heading("# 2", text="FName")
listbox.column("# 3", anchor=CENTER)
listbox.heading("# 3", text="LName")
listbox.column("# 4", anchor=CENTER)
listbox.heading("# 4", text="idk")
listbox.insert('', 'end', text="1", values=('1', 'Joe', 'Nash'))
listbox.insert('', 'end', text="2", values=('2', 'Emily', 'Mackmohan'))
listbox.insert('', 'end', text="3", values=('3', 'Estilla', 'Roffe'))
listbox.insert('', 'end', text="4", values=('4', 'Percy', 'Andrews'))
listbox.insert('', 'end', text="5", values=('5', 'Stephan', 'Heyward'))
listbox.pack()

if __name__ == "__main__":
    root.mainloop()

