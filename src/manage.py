import controls
import os,sys,select,time
from inputimeout import inputimeout
def PairDev():
    while True:
        [available_devices,device_id] = controls.SearchDevices()
        os.system('clear')
        print("\nAvailable devices for pairing: \n")
        for i in range(len(available_devices)):
            sys.stdout.write("\r{0} - {1}\n".format(i+1,available_devices[i]))
        try:
            option = int(inputimeout(prompt=">",timeout=4))
        except Exception:
            continue
        if option==-1:
            return None
        elif (option>=0 and option<len(available_devices)):
            print("Selected: ",available_devices[option-1])
            data = controls.PairDevice(device_id[option-1])
            out, err = data.communicate()
            out = out.decode()
            print(out)
            exit()
            os.system("sleep 4")
            if "Pairing successful" in out:
                return True
            return False



def PairedDevices():
    pairedDeviceList =  controls.PairedDevices()
    if len(pairedDeviceList) > 0:
        for device in pairedDeviceList:
            print("-> ",device)
    else:
        print("None")

def ResetDevice():
    return controls.UnpairDevices()
        

