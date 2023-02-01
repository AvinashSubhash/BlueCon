import controls
import os,sys,select,time
from inputimeout import inputimeout
def PairDev():
    while True:
        available_devices = controls.SearchDevices()
        os.system('clear')
        print("\nAvailable devices for pairing: \n")
        for i in range(len(available_devices)):
            sys.stdout.write("\r{0} - {1}\n".format(i+1,available_devices[i]))
        try:
            option = inputimeout(prompt=">",timeout=4)
            if option==-1:
                return None
            elif (option>=0 and option<len(available_devices)):
                print("Selected: ",available_devices[option][3])
                data = controls.PairDevice(available_devices[option][2])
                out, err = data.communicate()
                out = out.decode()
                if "Pairing successful" in out:
                    return True
                return False
        except Exception:
            pass


def PairedDevices():
    pairedDeviceList =  controls.PairedDevices()
    if len(pairedDeviceList) > 0:
        for device in pairedDeviceList:
            print("-> ",device)
    else:
        print("None")

def ResetDevice():
    return controls.UnpairDevices()
        

