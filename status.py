import os
import subprocess
def statusCheck():

    data = os.system("which bluetoothctl > output.txt")

    with open('output.txt') as file:
        data = file.readline()
    #print("data: ",data)
    data=str(data).split(":")
    #print("data :",data)
    if len(data[0])==0:
        return [False,"module 'which' or 'bluetoothctl' not installed."]
    else:
        return [True,"Installed"]

def ListPairedDevice():
    devices = subprocess.Popen(['ls','/home/kingaiva/new'],stdout=subprocess.PIPE)
    devices = list(devices.communicate())[0]
    if str(devices)=="b''":
        return []

    devices = str(devices).split("b'")[1].split("\\n")
    for x in range(len(devices)):
        devices[x] = devices[x].split(" ",2)
    devices.pop()
    return devices

ListPairedDevice()
statusCheck()