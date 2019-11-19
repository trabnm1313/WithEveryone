"""Prototype version of project"""
import os
def main():
    os.system("color a")
    total_styles = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [1, 3, 2], [1, 2, 3]]
    each_styles = []
    #SamplefromDatabaseFromExel
    styles = [["Hair", "Short", "Long", "Wavy"], ["Build", "Well-Build", "Plump", "Skinny"], ["Skin", "Pale", "Tanned", "Black"]]
    for style in styles:
        os.system("cls")
        print("\n\t" + style[0])
        for choice in range(1, len(style)):
            print("%d." %choice + style[choice])
        print()
        each_styles.append(int(input("What's your choice?: ")))
    os.system("cls")
    print("From following choices: \n")
    for style in range(len(each_styles)):
        print(styles[style][0] + ": " + styles[style][each_styles[style]])
    print("\nThere are " + str(total_styles.count(each_styles)) + " from " + str(len(total_styles)) + " people match your types.")

main()