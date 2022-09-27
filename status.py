import os

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

statusCheck()