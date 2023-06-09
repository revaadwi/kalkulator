from tkinter import*
import tkinter.font as font
import math

root = Tk()
root.title("KALKULATOR")
root["bg"] = "#F8AFA6"
root.geometry("330x410")

myfont  = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"]= myfont
e["bg"] = "#F9F1F0"
e.grid(row = 0, columnspan=4, pady=20, padx=20)

#untuk kolom angka
def cetak(nilai):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nilai))

#fungsi button
def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = float(nomor_awal)
    e.delete(0,END)

def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = float(nomor_awal)
    e.delete(0,END)

def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = float(nomor_awal)
    e.delete(0,END)

def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = float(nomor_awal)
    e.delete(0,END)


def hapus():
    e.delete(0,END)

def hapusSatu():
    current = e.get()
    e.delete(len(current)-1, END)

def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan":
        hitung= n_awal + float(nomor_akhir)
        hasil= round(hitung,5)
        e.insert(0,hasil)

    elif mtk == "pengurangan":
        hitung= n_awal - float(nomor_akhir)
        hasil= round(hitung,5)
        e.insert(0,hasil)

    elif mtk == "pembagian":
        try:
            hitung = n_awal / float(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,"Error")
            
    elif mtk == "perkalian":
        e.insert(0,n_awal * float(nomor_akhir))
    elif mtk == "desimal":
        e.insert(0,n_awal . float(nomor_akhir))

def desimal():
    current = e.get() 
    if '.' not in current:
        e.insert(END, '.')
    
#button
btn   = Button(root,text="1",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(1))
btn2  = Button(root,text="2",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(2))
btn3  = Button(root,text="3",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(3))
btn4  = Button(root,text="4",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(4))
btn5  = Button(root,text="5",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(5))
btn6  = Button(root,text="6",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(6))
btn7  = Button(root,text="7",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(7))
btn8  = Button(root,text="8",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(8))
btn9  = Button(root,text="9",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(9))
btn0  = Button(root,text="0",  padx = 30, bg="#FADCD9", fg="black", pady = 20, command=lambda:cetak(0))
tam   = Button(root,text="+",  padx = 30, bg="#F79489", fg="black", pady = 20, command=tambah  )
kur   = Button(root,text="-",  padx = 30, bg="#F79489", fg="black", pady = 20, command=kurang  )
bag   = Button(root,text="/",  padx = 30, bg="#F79489", fg="black", pady = 20, command=bagi    )
kal   = Button(root,text="x",  padx = 30, bg="#F79489", fg="black", pady = 20, command=kali    ) 
hap   = Button(root,text="C",  padx = 30, bg="#F79489", fg="black", pady = 20, command=hapus   )
dec   = Button(root,text=".",  padx = 32, bg="#F79489", fg="black", pady = 20, command=desimal )
hap1  = Button(root,text="<-", padx = 26, bg="#F79489", fg="black", pady = 20, command=hapusSatu )
equal = Button(root,text="=",  padx = 68, bg="#F79489", fg="black", pady = 20, command=samadengan)


#grid button
btn.grid   (row=1,column=0,pady=2)
btn2.grid  (row=1,column=1,pady=2)
btn3.grid  (row=1,column=2,pady=2)
btn4.grid  (row=2,column=0,pady=2)
btn5.grid  (row=2,column=1,pady=2)
btn6.grid  (row=2,column=2,pady=2)
btn7.grid  (row=3,column=0,pady=2)
btn8.grid  (row=3,column=1,pady=2)
btn9.grid  (row=3,column=2,pady=2)
btn0.grid  (row=4,column=1,pady=2)

#grid fungsi button
tam.grid   (row=5,column=1,pady=2)
kur.grid   (row=2,column=3,pady=2)
bag.grid   (row=3,column=3,pady=2)
kal.grid   (row=4,column=3,pady=2)
hap.grid   (row=4,column=0,pady=2)
hap1.grid  (row=1,column=3,pady=2)
dec.grid   (row=4,column=2,pady=2)
equal.grid (row=5,column=2,columnspan=2)


root.mainloop()