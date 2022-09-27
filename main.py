import status
import os
MENU_OPTIONS = ["Pair a Device","Connect a Device","Disconnect a Device","Clear Data","Exit"]
while True:
    os.system("clear")
    #Display graphics
    print("BlueCon\n")
    #Display Bluetooth status
    for i in range(len(MENU_OPTIONS)):
        print(i+1,MENU_OPTIONS[i])

    print("\n>",end="")
    option = int(input())
    if option==1:
        os.system("clear")
        Graphics()
        PairDevice()
    elif option==2:
        os.system("clear")
        Graphics()
        ConnectDevice()
    elif option==3:
        os.system("clear")
        Graphics()
        DisconnectDevicc()
    elif option==4:
        os.system("clear")
        Graphics()
        #Script to clear the pair status
        pass
    elif option==5:
        os.system("clear")
        exit()