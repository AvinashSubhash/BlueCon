import status
import os
MENU_OPTIONS = ["Connect a Device","Disconnect a Device","Clear Data"]
while True:
    os.system("clear")
    #Display graphics
    print("BlueCon\n")
    #Display Bluetooth status
    for i in range(len(MENU_OPTIONS)):
        print(i+1,MENU_OPTIONS[i])

    print("\n>",end="")
    data = input()