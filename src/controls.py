import subprocess
import os
devices=[]
final_result=[]
def ConnectDevice():
    pass

def SearchDevices():
    os.system("timeout 5s bluetoothctl scan on > devices.txt")    
    file_data=[]
    with open("devices.txt") as file:
        file_data.append(list((file.readlines())))
    file_data = file_data[0][2:]
    for i in range(len(file_data)):
        file_data[i] = file_data[i].split(" ",3)
        if file_data[i][2] not in devices:
            devices.append(file_data[i][2])
            final_result.append(file_data[i][3])
    return final_result

def PairDevice(macAddr):
    pairing_status = subprocess.Popen(['bluetoothctl','pair',str(macAddr)],stdout=subprocess.PIPE)
    return pairing_status

def PairedDevices():
    data = subprocess.Popen(['bluetoothctl','paired-devices'],stdout=subprocess.PIPE)
    out, err = data.communicate()
    #print(out,"\ntesting\n")
    out = out.decode().split(" ",2)[2]
    return out