from tkinter import *
from tkinter import messagebox
import random
import string

def gen_fun():
    len = int(len_input.get())
    if len <= 0:
        messagebox.showerror('ERROR','Enter a valid length')
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(len))
        pw_outout_label.config(text=password)

def accept_fun():
    final_pw = pw_outout_label.cget("text")
    pw_outout_label.config(text='')
    len_input.delete(0, END)
    messagebox.showinfo('Your password is ',final_pw)

def clear_fun():
    pw_outout_label.config(text='')
    len_input.delete(0, END)

root = Tk()
root.geometry('450x570')
root.resizable(0,0)
root.configure(background='grey')
root.title('Password Generator')

title_label = Label(root, text='PASSWORD GENERATOR', bg='grey', fg='navy')
title_label.config(font=('verdana',18,'bold','underline'))
title_label.pack(padx=(50,10), pady=(50,50))

len_label = Label(root, text='Enter password length :',bg='grey', fg='black')
len_label.config(font=('verdana',10))
len_label.pack(padx=(20,10), pady=(10,10))

len_input = Entry(root, width= 35)
len_input.pack(ipady=5, padx=(35), pady=(10,10))

pw_label = Label(root, text='Generated Password ',bg='grey', fg='black')
pw_label.pack(pady=(10,10))

pw_outout_label = Label(root, text='', width=35)
pw_outout_label.pack(pady=(10,20), ipady=5)

gen_btn = Button(root, text='Generate', bg='navy', fg='white', width=12, height=2, command=gen_fun)
gen_btn.config(font=('verdana',8,'bold'))
gen_btn.pack(pady=(20,10))

accept_btn = Button(root, text='Accept', bg='white', fg='navy', width=8, height=1, command=accept_fun)
accept_btn.config(font=('verdana',8,'bold'))
accept_btn.pack(pady=(10,10))

reset_btn = Button(root, text='Reset', bg='white', fg='navy', width=8, height=1, command=clear_fun)
reset_btn.config(font=('verdana',8,'bold'))
reset_btn.pack(pady=(10,10))


root.mainloop()
