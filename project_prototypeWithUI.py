from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from openpyxl import load_workbook
workbook = load_workbook(filename="styles.xlsx")
local_sheet = workbook.active
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
sheet = gspread.authorize(credentials).open_by_url("https://docs.google.com/spreadsheets/d/15tCtq2eCq-eHpejuM82MVq6Y2xCHYXj3febatdVpevg/edit#gid=1403196604")
worksheet = sheet.get_worksheet(0)

def makeData():
    for row in range(2, len(worksheet.col_values(1))+1):
        if worksheet.row_values(row)[1:] != []:
            data_x.append(worksheet.row_values(row)[1:])
def makeStyles():
    for row in range(1, len(local_sheet["A"])+1):
        datalist = []
        if type(local_sheet["A" + str(row)].value) != type(None):
            for col in range(2, len(local_sheet[str(row)])+1):
                if type(local_sheet[chr(64 + col) + str(row)].value) != type(None):
                    datalist.append(local_sheet[chr(64 + col) + str(row)].value)
            styles[local_sheet["A" + str(row)].value] = datalist
    print(styles)

#Def function but idk why it's here
def callback(var):
    data_input.append(var)
    intvar.set(0)

#Def ui variable
ui = Tk()
ui.title("EIEI")

#Samples data from database
styles = {}
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
    texts = {}
    text['text'] = "What " + var + " style would you prefer?"
    for index in range(1, len(styles[var])+1):
        buttons[index] = Button(text=index, command=lambda style=styles[var][index-1]: callback(style), width=5, height=2)
        buttons[index].grid(row=index+1, column=0, pady=2)
    for index in range(1, len(styles[var])+1):
        texts[index] = Label(text=styles[var][index-1])
        texts[index].grid(row=index+1, column=1, pady=2)
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
    for txt in texts:
        texts[txt].grid_forget()

def main():
    makeData()
    makeStyles()
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
