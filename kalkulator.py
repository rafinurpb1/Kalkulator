from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("Kalkulator Piton")
root["bg"] = "#e5ffff"
root.geometry("310x410")

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["bg"] = "#e5ffff"
e.grid(row=0, columnspan=4, pady=25, padx=20)

def cetak(nilai):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(nilai))

def tambah():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "jumlah"
    b_awl = float(blgnawal)
    e.delete(0, END)

def kurang():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "kurang"
    b_awl = float(blgnawal)
    e.delete(0, END)

def kali():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "kali"
    b_awl = float(blgnawal)
    e.delete(0, END)

def bagi():
    blgnawal = e.get()
    global b_awl
    global mat
    mat = "bagi"
    b_awl = float(blgnawal)
    e.delete(0, END)

def hapus():
    e.delete(0, END)


def samadengan():
    b_akhr = e.get()
    e.delete(0, END)
    if mat == "jumlah":
        e.insert(0, b_awl + float(b_akhr))
    elif mat == "kurang":
        e.insert(0, b_awl - float(b_akhr))
    elif mat == "bagi":
        try:
            hitung = b_awl / float(b_akhr)
            e.insert(0, hitung)
        except ZeroDivisionError:
            e.insert(0, "Tidak Bisa Dibagi 0")

    elif mat == "kali":
        e.insert(0, b_awl * float(b_akhr))


tbl = Button(
    root, text="1", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(1)
)
tbl2 = Button(
    root, text="2", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(2)
)
tbl3 = Button(
    root, text="3", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(3)
)
tbl4 = Button(
    root, text="4", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(4)
)
tbl5 = Button(
    root, text="5", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(5)
)
tbl6 = Button(
    root, text="6", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(6)
)
tbl7 = Button(
    root, text="7", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(7)
)
tbl8 = Button(
    root, text="8", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(8)
)
tbl9 = Button(
    root, text="9", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(9)
)
tbl0 = Button(
    root, text="0", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak(0)
)
tbltitik = Button(
    root, text=".", padx=30, bg="#4664AF", fg="white", pady=20, command=lambda: cetak("."),
)
tam = Button(root, text="+", padx=30, bg="#18A5AC", fg="white", pady=20, command=tambah)
kur = Button(root, text="-", padx=30, bg="#18A5AC", fg="white", pady=20, command=kurang)
bag = Button(root, text="÷", padx=30, bg="#18A5AC", fg="white", pady=20, command=bagi)
kal = Button(root, text="x", padx=30, bg="#18A5AC", fg="white", pady=20, command=kali)
samdeng = Button(root, text="=", padx=30, bg="#d1c4e9", pady=20, command=samadengan)
hap = Button(root, text="C", padx=150, bg="#ff1744", pady=20, command=hapus)

tbl.grid(row=3, column=0, pady=2)
tbl2.grid(row=3, column=1, pady=2)
tbl3.grid(row=3, column=2, pady=2)
tbl4.grid(row=2, column=0, pady=2)
tbl5.grid(row=2, column=1, pady=2)
tbl6.grid(row=2, column=2, pady=2)
tbl7.grid(row=1, column=0, pady=2)
tbl8.grid(row=1, column=1, pady=2)
tbl9.grid(row=1, column=2, pady=2)
tbl0.grid(row=4, column=0, pady=2)
tbltitik.grid(row=4, column=1, pady=2)

bag.grid(row=1, column=3, pady=2)
kur.grid(row=2, column=3, pady=2)
kal.grid(row=3, column=3, pady=2)
tam.grid(row=4, column=3, pady=2)
samdeng.grid(row=4, column=2, pady=2)
hap.grid(row=5, column=0, columnspan=4)

root.mainloop()
