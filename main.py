from tkinter import *
import os

def doChangeTransparency(event):
    amount = entry1.get()
    command = '"' + "sh -c 'xprop -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * "+amount+" / 100)))'" + '"'
    os.system("gnome-terminal --command="+command)

def makeOpaque(event):
    command = '"' + "sh -c 'xprop -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * 100 / 100)))'" + '"'
    os.system("gnome-terminal --command="+command)

def makeTransparent(event):
    command = '"' + "sh -c 'xprop -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * 0 / 100)))'" + '"'
    os.system("gnome-terminal --command="+command)

window = Tk()
window.title('Translucency Tweaker')

mainFrame = Frame(window, width=100)
mainFrame.pack(side = 'top')

label1 = Label(mainFrame,text='Enter value of opacity in percentage : ')
label1.grid(row = 0, column = 0)

entry1 = Entry(mainFrame)
entry1.grid(row = 0, column = 1)

bottomFrame = Frame(window, width = 100)
bottomFrame.pack(side = 'bottom')

button1 = Button(mainFrame, text = 'Apply')
button1.bind('<Button-1>',doChangeTransparency)
button1.grid(row = 3, columnspan = 2)

label2 = Label(bottomFrame, text = 'Other Options')
label2.pack()

button2 = Button(bottomFrame, text = 'Make Completely Opaque')
button2.bind('<Button-1>',makeOpaque)
button2.pack()

button3 = Button(bottomFrame, text = 'Make Completely Transparent')
button3.bind('<Button-1>',makeTransparent)
button3.pack()

finalLabel = Label(bottomFrame,text = 'After selecting desired option, click on the window you want to apply translucency tweaks to')
finalLabel.pack()

window.mainloop()