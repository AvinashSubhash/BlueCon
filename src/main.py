import status
import os
import manage
MENU_OPTIONS = ["Pair a Device","Connect a Device","Disconnect a Device","Clear Data","Exit"]
os.system("bluetoothctl power on")

while True:
    os.system("clear")
    #Display graphics
    print("BlueCon\n")
    #Display Bluetooth status
    print("Paired Devices : ")
    manage.PairedDevices()
    print("\n\n")
    for i in range(len(MENU_OPTIONS)):
        print(i+1,MENU_OPTIONS[i])

    print("\n>",end="")
    option = int(input())
    if option==1:
        os.system("clear")
        #Graphics()
        manage.PairDev()
    elif option==2:
        os.system("clear")
        Graphics()
        #ConnectDevice()
    elif option==3:
        os.system("clear")
        Graphics()
        DisconnectDevice()
    elif option==4:
        os.system("clear")
        #Graphics()
        manage.ResetDevice()
        pass
    elif option==5:
        os.system("clear")
        exit()