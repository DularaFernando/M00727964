import tkinter as tk

window = tk.Tk() #object that is root window
window.title('Tkinter hello world')

text = tk.Label(text = "What's your name", foreground ='white', background = 'blue',
                width = 30, height = 3)

#text.pack()

entry = tk.Entry(width = 30)
#entry.pack()

def save_and_print():
    name = entry.get()
    entry.delete(0, tk.END)
    print(name)

button = tk.Button(text = 'Submit', width = 30, height = 5,
                   command = save_and_print)
#button.pack(padx = 5, pady = 5)

#window.blind('<Return>',save_and_print)
window.bind('<Return>', lambda event:save_and_print()) #if func need parameters

frame = tk.Frame(master = window)
frame = tk.Label(master = frame, text = 'Frame!')

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 3)

text.grid(column = 0, row = 0, padx = 5, pady = 5)
entry.grid(column = 0, row = 1, padx = 5, pady = 5)
button.grid(column = 1, row = 0, padx = 5, pady = 5)
label.grid(column = 1, row = 1, padx = 5, pady = 5)

window.mainloop() #start event loop, method on top of 'window'
