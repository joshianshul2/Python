from tkinter import *
from PIL import Image,ImageTk # pil: python imaging library and tkintertk helps to take jpg file

anji = Tk()

anji.geometry("455x555")
#photo=PhotoImage(file="sm.png") // not suppoted
# for jpg image and all !!!
image=Image.open("abc.png")
photo=ImageTk.PhotoImage(image)
anshul_label = Label(image=photo)
anshul_label.pack()


anji.mainloop()
