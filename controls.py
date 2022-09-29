import subprocess
import os

def ConnectDevice():
    pass

def PairDevice():
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
PairDevice()
