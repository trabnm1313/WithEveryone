from tkinter import *
from openpyxl import load_workbook
workbook = load_workbook(filename="GG.xlsx")
sheet = workbook.active

def makeData():
    for row in range(2, len(sheet["A"])+1):
        datalist = []
        for col in range(2, len(sheet["1"])+1):
            datalist.append(sheet[chr(col + 64) + str(row)].value)
        data_x.append(datalist)


#Def function but idk why it's here
def callback(var):
    data_input.append(var)
    intvar.set(0)

#Def ui variable
ui = Tk()

#Samples data from database
styles = {"Hair": ["Short", "Long", "Wavy"], "Build": ["Well-Build", "Plump", "Skinny", "Fat"], "Skin": ["Pale", "Tanned", "Black"], "Height": ["High", "Middle", "Short"], "Weight": ["High", "Middle", "Low"]}
data_x = []

#Variable
data_input = []
buttons = dict()
intvar = IntVar()
text = Label(text="Welcome to personal preference analysis program!.", anchor=CENTER, font=("AngsanaUPC", 18))
text2 = Label(text="", anchor=CENTER, font=("AngsanaUPC", 18))
text.grid(row=0, column=0, columnspan=8, padx=80)
text2.grid(row=1, column=0, columnspan=8, padx=80)

#Def function and call function
def choice(var):
    count = 0
    buttons = {}
    text['text'] = "What " + var + " style would you prefer?"
    for index in range(1, len(styles[var])+1):
        buttons[index] = Button(text=index, command=lambda style=styles[var][index-1]: callback(style), width=5, height=2)
        buttons[index].grid(row=index+1, column=0, pady=2)
    ui.wait_variable(intvar)
    for data in data_x:
        brk = 0
        for char in range(len(data_input)):
            print(data[char], data_input[char])
            if data[char] != data_input[char]:
                brk = 1
        if brk == 0:
            count += 1
    text2['text'] = "There is " + str(count) + " match you choice out of " + str(len(data_x))

    for button in buttons:
        buttons[button].grid_forget()

def main():
    makeData()
    print(data_x)
    ppl = 0
    keep = -1
    startbtn = Button(text="Click here to start", command=lambda: intvar.set(0))
    startbtn.grid(row=2, column=3, padx=80)
    ui.wait_variable(intvar)
    startbtn.grid_forget()

    for style in styles:
        choice(style)

    if data_x.count(data_input) > 0:
        text2['text'] = "There is " + str(data_x.count(data_input)) + " people match you styles out of " + str(len(data_x)) + "!"
    else:
        text2['text'] = "Sorry, You styles is not match any people in our data."


    text['text'] = "Thanks for making surveys."
    print(data_input)

#Call main() and UI.mainloop()
main()
ui.mainloop()
