from tkinter import *

firstNum = secondNum = operator = NONE

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global firstNum, operator
    firstNum = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global firstNum, secondNum, operator
    secondNum = int(result_label['text'])
    if operator ==  '+':
        result_label.config(text=str(firstNum+secondNum))
    elif operator == '-':
        result_label.config(text=str(firstNum-secondNum))
    elif operator == '*':
        result_label.config(text=str(firstNum*secondNum))
    elif operator == '/':
        result_label.config(text=str(round(firstNum/secondNum , 3)))
    elif secondNum == '':
        result_label.config(text="ERROR")
    else:
        result_label.config(text='ERROR')

root = Tk()

root.title('Calculator')
root.geometry('300x380')
root.resizable(0,0)
root.configure(background='#d1e890')

result_label = Label(root, text='', bg='#d1e890', fg='white')
result_label.grid(row=0,column=0, columnspan=5,sticky='w', pady=(50,25))
result_label.config(font=('verdana',30,'bold'))

btn7 = Button(root, text='7', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14,'bold'))

btn8 = Button(root, text='8', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14,'bold'))

btn9 = Button(root, text='9', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14,'bold'))

btn_add = Button(root, text='+', bg='#ab8d8a',fg='white',width=5, height=2, command= lambda : get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14,'bold'))

btn4 = Button(root, text='4', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14,'bold'))

btn5 = Button(root, text='5', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14,'bold'))

btn6 = Button(root, text='6', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14,'bold'))

btn_sub = Button(root, text=' -', bg='#ab8d8a',fg='white',width=5, height=2, command= lambda : get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14,'bold'))

btn1 = Button(root, text='1', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14,'bold'))

btn2 = Button(root, text='2', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14,'bold'))

btn3 = Button(root, text='3', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14,'bold'))

btn_mul = Button(root, text='*', bg='#ab8d8a',fg='white',width=5, height=2, command= lambda : get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14,'bold'))

btn_clr = Button(root, text='C', bg='#ab8d8a',fg='white',width=5, height=2, command=clear)
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14,'bold'))

btn0 = Button(root, text='0', bg='#32a893',fg='white',width=5, height=2, command=lambda : get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14,'bold'))

btn_eq = Button(root, text='=', bg='#ab8d8a',fg='white',width=5, height=2, command=get_result)
btn_eq.grid(row=4,column=2)
btn_eq.config(font=('verdana',14,'bold'))

btn_div = Button(root, text='/', bg='#ab8d8a',fg='white',width=5, height=2, command= lambda : get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14,'bold'))


root.mainloop()