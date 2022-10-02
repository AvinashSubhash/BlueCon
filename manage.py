import controls
def PairDev():
    available_devices = controls.SearchDevices()
    print("\nAvailable devices for pairing: \n")
    for i in range(len(available_devices)):
        print(i,". ",available_devices[i][3])
    print("\nEnter the device to pair (-1 to exit):")
    option = int(input())
    if(option>=0 and option<len(available_devices)):
        print("Selected: ",available_devices[option][3])
        data = controls.PairDevice(available_devices[option][2])
        out, err = data.communicate()
        out = out.decode()
        if "Pairing successful" in out:
            return True
        return False

def PairedDevices():
    return controls.PairedDevices()
        

