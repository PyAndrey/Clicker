from tkinter import *

window = Tk()
window.eval('tk::PlaceWindow %s center' %
            window.winfo_pathname(window.winfo_id()))
window.title("Clicker")
window.geometry("510x280")
window.resizable(0, 0)
clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn1.configure(text=clicks)


btn1 = Button(window, text=0, activebackground="#ADFF2F",
              background="#7CFC00", foreground="#FF00FF", font="100", command=click_button)
btn1.pack(expand=True, fill=BOTH)


window.mainloop()
