import Tkinter as T


def volume(length, enter_concetration, result_moles):
    return length*0.66*result_moles/enter_concetration


def load():
    lvector = float(entery_lv.get())
    cvector = float(entery_cv.get())
    linsert = float(entery_li.get())
    cinsert = float(entery_ci.get())
    return lvector, cvector, linsert, cinsert


def recipe(tabele):
    vvector = round(volume(tabele[0], tabele[1], 0.02), 2)
    vinsert = round(volume(tabele[2], tabele[3], 0.06), 2)
    h2o = round(float(17.-vvector-vinsert), 2)
    a = "Przepis na udana ligacje to:\n\n"
    b = "Woda----%.2f ul\n" % h2o
    c = "Bufor do ligacji----2 ul\n"
    d = "Wstawka----%.2f ul\n" % vinsert
    e = "Wektor----%.2f ul\n" % vvector
    f = "Ligaza----1 ul\n"
    return a+b+c+d+e+f


def maine(event):
    resultFrame = T.Frame(root)
    resultFrame.pack(side='bottom')
    resultLabel = T.Label(resultFrame, text=recipe(load()))
    resultLabel.pack()




root = T.Tk()
welcomeLabel=T.Label(root, text='Program LigCal zwraca sklad mieszaniny ligacyjnej\n\
z 0.06 pmol wstawki i 0.02 pmol wektora.\n Koncowa objetos mieszaniny to 20 ul\n')
welcomeLabel.pack(side='top')
frame = T.Frame(root)
frame.pack()
label_lv = T.Label(frame, text='Wielkosc wektora w b.p.:')
label_cv = T.Label(frame, text='Stezenie wektora w ng/ul:')
label_li = T.Label(frame, text='Wielkosc wstawki w b.p.:')
label_ci = T.Label(frame, text='Stezenie wstawki w ng/ul:')
entery_lv = T.Entry(frame)
entery_cv = T.Entry(frame)
entery_li = T.Entry(frame)
entery_ci = T.Entry(frame)

label_lv.grid(row=0, sticky='w')
label_cv.grid(row=1, sticky='w')
label_li.grid(row=2, sticky='w')
label_ci.grid(row=3, sticky='w')
entery_lv.grid(row=0, column=1)
entery_cv.grid(row=1, column=1)
entery_li.grid(row=2, column=1)
entery_ci.grid(row=3, column=1)
button1 = T.Button(root, text="Oblicz")
button1.bind("<Button-1>", maine)
button1.pack(side='left')

photo = T.PhotoImage(file='symbol.png')
label = T.Label(root, image=photo)
label.pack(side='right')

root.mainloop()
