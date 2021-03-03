import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import json

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data = params    #Gets all the values from the url and stores in json format and stores in data var
        self.currencies = self.data['rates']    
    def convert(self, from_currecy, to_currency, amount):
        initial_amount = amount
        # Here we will convert everything to USD and 
        # Then convert it in the required format
        if from_currecy!='United States Dollar':
            amount = amount/self.currencies[from_currecy]

        amount = round(amount*self.currencies[to_currency], 10) # Rounding it to 10 decimal places
        return amount



# Creating GUI
class App(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        # self.configure(background = 'blue')
        self.geometry("605x250")
        
        # Label
        self.intro_label = Label(self, text = 'Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))

        self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('Indian Rupee','United States Dollar',1)} United States Dollar \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        self.date_label.config(font = ('Courier',10,'bold'))
        self.intro_label.place(x = 115 , y = 5)
        self.date_label.place(x = 50, y= 50)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("Indian Rupee") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("United States Dollar") # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 20, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 20, justify = tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y= 120)
        self.amount_field.place(x = 70, y = 150)
        self.to_currency_dropdown.place(x = 340, y= 120)
        
        self.converted_amount_field_label.place(x = 380, y = 150)
        
        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Courier', 15, 'bold'))
        self.convert_button.place(x = 260, y = 200)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 10)

        self.converted_amount_field_label.config(text = str(converted_amount))
    
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    with open("currency.json","r") as c:
        params = json.load(c)["params"]
    
    url = params
   
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()