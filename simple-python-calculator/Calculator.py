# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:40:52 2020

@author: Soumaia Bouhouia
"""
from tkinter import Tk, Entry, Button, N, E, S, W, StringVar

class CalGUI:
    result: float
    operand: StringVar
    equation: StringVar
    
    def operandValid(self, text):
        try:
            float(text)
            return True
               
        except:
            return False
        
    def press(self, num):
        
        value = self.operand.get() + str(num)
        self.operand.set(value)
        
        if self.operandValid(value) == True:
            self.operand.set(value)
            
        elif self.operandValid(value) == False:
            self.operand.set("")#reset the Entry for new input

            
    def add(self):
        first_number = self.operand.get()
        global f_num
        global operation
        operation = "addition"
        f_num = float(first_number)
        self.operand.set("")
    
    def substract(self):
        first_number = self.operand.get()
        global f_num
        global operation
        operation = "substraction"
        f_num = float(first_number)
        self.operand.set("")
        
    def multiply(self):
        first_number = self.operand.get()
        global f_num
        global operation
        operation = "multiplication"
        f_num = float(first_number)
        self.operand.set("")

    def divide(self):
        first_number = self.operand.get()
        global f_num
        global operation
        operation = "division"
        f_num = float(first_number)
        self.operand.set("")        
        
    def equal(self):
        second_number = self.operand.get()
        self.operand.set("")
        
        if operation == "addition":
            self.operand.set(f_num + float(second_number))
                    
        if operation == "substraction":
            self.operand.set(f_num - float(second_number))
                    
        if operation == "multiplication":
            self.operand.set(f_num * float(second_number))
        
        if operation == "division":
            self.operand.set(f_num / float(second_number))
        
    
    def __init__(self):
        master = Tk()
        master.title("Calculator")
        
        self.operation = StringVar()
        self.operand=StringVar()
        addAction = lambda : self.add()
        substractAction = lambda : self.substract()
        divideAction = lambda : self.divide()
        multiplyAction = lambda : self.multiply()
        equalAction = lambda : self.equal()

            
        vcmd = master.register(self.operandValid)

        Entry(master, validate="key", validatecommand=(vcmd, '%P'), textvariable=self.operand).grid(row=1, column=0, columnspan =4)
        Button(master, text = "1", command=lambda:self.press(1)).grid(row=2,column=0, sticky = N+S+E+W)
        Button(master, text = "2", command=lambda:self.press(2)).grid(row=2,column=1, sticky = N+S+E+W)
        Button(master, text = "3", command=lambda:self.press(3)).grid(row=2,column=2, sticky = N+S+E+W)
        Button(master, text = "+", command=addAction).grid(row=2,column=3, sticky = N+S+E+W)
        Button(master, text = "4", command=lambda:self.press(4)).grid(row=3,column=0, sticky = N+S+E+W)
        Button(master, text = "5", command=lambda:self.press(5)).grid(row=3,column=1, sticky = N+S+E+W)
        Button(master, text = "6", command=lambda:self.press(6)).grid(row=3,column=2, sticky = N+S+E+W)
        Button(master, text = "-", command=substractAction).grid(row=3,column=3, sticky = N+S+E+W)
        Button(master, text = "7", command=lambda:self.press(7)).grid(row=4,column=0, sticky = N+S+E+W)
        Button(master, text = "8", command=lambda:self.press(8)).grid(row=4,column=1, sticky = N+S+E+W)
        Button(master, text = "9", command=lambda:self.press(9)).grid(row=4,column=2, sticky = N+S+E+W)
        Button(master, text = "x", command=multiplyAction).grid(row=4,column=3, sticky = N+S+E+W)
        Button(master, text = "0", command=lambda:self.press(0)).grid(row=5,column=0, sticky = N+S+E+W)
        Button(master, text = ".", command=lambda:self.press('.')).grid(row=5,column=1, sticky = N+S+E+W)
        Button(master, text = "=", command=equalAction).grid(row=5,column=2, sticky = N+S+E+W)
        Button(master, text = "/", command=divideAction).grid(row=5,column=3, sticky = N+S+E+W)
        
          
        master.mainloop()


CalGUI()
        