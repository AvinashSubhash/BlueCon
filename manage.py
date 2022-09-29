import controls
def PairDev():
    available_devices = controls.PairDevice()
    print("\nAvailable devices for pairing: \n")
    for i in range(len(available_devices)):
        print(i,". ",available_devices[i][3])
    print("\nEnter the device to pair (-1 to exit):")
    option = int(input())
    if(i>=0 and i<len(available_devices)):
        print("Selected: ",available_devices[i][3])
    
