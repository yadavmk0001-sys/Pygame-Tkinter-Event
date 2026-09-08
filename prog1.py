from tkinter import *

window = Tk()
window.title("Event Handler.")
window.geometry("500x500")

def handle(event):
    print(event.char)

window.bind("<Key>", handle)
def handle_click(event):
    print("\nThe button was clicked.")

button = Button(text="Hello!")
button.pack()

button.bind("<Button>", handle_click)

window.mainloop()