import subprocess
import os

FINAL_DEVICE_ID=[]
FINAL_DEVICE_NAMES=[]
PAIRED_DEVICE_NAMES=[]
PAIRED_DEVICE_ID=[]
def ConnectDevice(macAddr):
    connecting_status = subprocess.Popen(['bluetoothctl','connect',str(macAddr)],stdout=subprocess.PIPE)
    return connecting_status

def SearchDevices():
    os.system("timeout 5s bluetoothctl scan on > devices.txt")    
    file_data=[]
    with open("devices.txt") as file:
        file_data.append(list((file.readlines())))
    file_data = file_data[0][2:]
    for i in range(len(file_data)):
        file_data[i] = file_data[i].split(" ",3)
        if file_data[i][0]=="[[0;92mNEW[0m]" and file_data[i][2] not in FINAL_DEVICE_ID:
            FINAL_DEVICE_ID.append(file_data[i][2])
            FINAL_DEVICE_NAMES.append(file_data[i][3])
    os.system("bluetoothctl scan off")
    return [FINAL_DEVICE_NAMES,FINAL_DEVICE_ID]

def PairDevice(macAddr):
    pairing_status = subprocess.Popen(['bluetoothctl','pair',str(macAddr)],stdout=subprocess.PIPE)
    out, err = pairing_status.communicate()
    out = out.decode()
    if "Pairing successful" in out:
        return ConnectDevice(macAddr)
    return pairing_status

def PairedDevices():
    data = subprocess.Popen(['bluetoothctl','paired-devices'],stdout=subprocess.PIPE)
    out, err = data.communicate()
    out = out.decode().split("\n")[:-1]
    for i in range(len(out)):
        out[i] = out[i].split(" ",2)
        PAIRED_DEVICE_NAMES.append(out[i][1])
        PAIRED_DEVICE_ID.append(out[i][0])
        out[i] = out[i][2]
    return out

def UnpairDevices():
    for device in PAIRED_DEVICE_NAMES:
        data = subprocess.Popen(['bluetoothctl','remove',device],stdout=subprocess.PIPE)
        data,err = data.communicate()
        print(data.decode())
    while len(PAIRED_DEVICE_NAMES)>0:
        PAIRED_DEVICE_NAMES.pop(0)
        PAIRED_DEVICE_ID.pop(0)
