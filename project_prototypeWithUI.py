from tkinter import *

#Def function but idk why it's here
def callback(var):
    data_input.append(var)
    intvar.set(0)

#Def ui variable
ui = Tk()

#Samples data from database
styles = {"Hair": ["Short", "Long", "Wavy"], "Build": ["Well-Build", "Plump", "Skinny", "Fat"], "Skin": ["Pale", "Tanned", "Black"]}
data_x = [[1, 2, 3], [3, 2, 1], [3, 3, 3], [1, 2, 3]]

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
        buttons[index] = Button(text=index, command=lambda num=index: callback(num), width=5, height=2)
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
