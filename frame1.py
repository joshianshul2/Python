from tkinter import *
root=Tk()

root.geometry("700x700")

f1=Frame(root,bg="red",borderwidth=1,padx='50')
f1.pack(side=LEFT,fill="y")
l1=Label(f1,text="Anji",fg="cyan",bg="black").pack(padx="21",pady="190")
#l2=Label(text="Anshul",fg="red",bg="blue").pack(padx="96",pady="99")
f2=Frame(root,bg="cyan",borderwidth=2,padx='100',pady='25')
f2.pack(side=TOP,fill='x')
l2=Label(f2,text="Anshul Is using Tkinter",fg="black",bg="yellow",font='arial 21 bold').pack()

# font syntex is font word size type;

root.mainloop()

#dsc in x padding
