from tkinter import *
def submit() :
    c=u. get ()
    b=""
    for i in range (len(c)):
        if ' a'<=c[i]<='w' or ' A' <=c[i]<=' W':
            b=b+chr (ord(c[i]) +3)
        elif ' x'<=c[i]<=' z' or ' X'<=c[i]<=' Z' :
            b=b+chr (ord(c[i])-23)
        else:
            b=b+c[i]
    p. set (str (b))
root = Tk()
root. title("凯撒加密")
frame = Frame (root)
frame. pack (padx=8，pady=8， ipadx=4)
lab1 = Label (frame, text="请输入明文")
lab1. grid (row=0，column=0， padx=5， pady=5， sticky=W)
u= StringVar()
ent1 = Entry (frame， textvariable=u, width=30)
ent1. grid (row=0，column=1， sticky=' ew' ，columnspan=2)
lab2 = Label (frame，text="凯撒密文")
lab2. grid (row=1，column=0， padx=5， pady=5， sticky=W)
p = StringVar()
ent2 = Entry (frame， textvariable=p, width=30)
ent2. grid (row=1，column=1， sticky=' ew'，columnspan=2)
button = Button (frame，text=" 加密"，command=submit， default=' active' )
button. grid(row=2，column=1)
root. mainloop ()
