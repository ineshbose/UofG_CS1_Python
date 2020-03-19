
import tkinter

def display():
    messageLabel.configure(text="Hello World!")

top = tkinter.Tk()

messageLabel = tkinter.Label(top,text="")
messageLabel.grid()

showButton = tkinter.Button(top,text="Show",command=display)
showButton.grid()

quitButton = tkinter.Button(top,text="Quit",command=top.destroy)
quitButton.grid()

tkinter.mainloop()
