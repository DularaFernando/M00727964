import tkinter as tk

window = tk.Tk() #object that is root window
window.title('Tkinter hello world')

text = tk.Label(text = 'Hello world')

text.pack()


window.mainloop() #start event loop, method on top of
