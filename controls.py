import subprocess
import os

def ConnectDevice():
    pass

def SearchDevices():
    os.system("timeout 5s bluetoothctl scan on > devices.txt")    
    devices=[]
    with open("devices.txt") as file:
        devices.append(list((file.readlines())))
    devices = devices[0]
    final_result=[]
    for i in range(len(devices)):
        devices[i] = devices[i].split(" ",3)
        #print(devices[i][0])
        if "NEW" in devices[i][0]:
            final_result.append(devices[i])
    return final_result

def PairDevice(macAddr):
    pairing_status = subprocess.Popen(['bluetoothctl','pair',str(macAddr)],stdout=subprocess.PIPE)
    return pairing_status

def PairedDevices():
    data = subprocess.Popen(['bluetoothctl','devices'],stdout=subprocess.PIPE)
    out, err = data.communicate()
    #print(out,"\ntesting\n")
    out = out.decode()
    return out