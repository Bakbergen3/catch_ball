import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width=20)
b = tk.Button(root, text='Transform')
l = tk.Label(root, bg='black', fg='white', width=20)


def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortlist)

e.pack()
b.pack()
l.pack()

root.mainloop()