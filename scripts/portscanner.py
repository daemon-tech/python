import pyfiglet
import sys
import subprocess
import socket
from datetime import datetime

#cls screen
subprocess.call('clear', shell=True)

ascii_banner = pyfiglet.figlet_format("Port Scanner")

#colors
r = "\033[1;31;40m"
g = "\033[1;32;40m"
b = "\033[1;34;40m"
white =  "\033[1;37;40m"
purple = "\033[1;35;40m"

#banner -credits
print(g,"Portscanner by OSzer0day \n")
print(purple, ascii_banner)

#input
hostserver = input("Enter host to scan: ")
hostserverip = socket.gethostbyname(hostserver)

#informations output 

print(white,"-" * 60)
print("Scanning the hostserver: ", hostserverip)
print("-" * 60)

#scan started @ what time
t1 = datetime.now()

#specify ports

try:
	for port in range(1,1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((hostserverip, port))
		if result == 0:
			print(g, "Port {}:  Open".format(port))
		sock.close()
except KeyBoardInterrupt:
	print(r, "Your pressed Ctrl+C")
	sys.exit()
except socket.gaierror:
	print(r, "Hostname could not been resolved. Closing")
except socket.error:
	print(r, "Couldn´t connect to server")

#checking time again
t2 = datetime.now()

#calculating difference of time
total = t2 - t1

#printing inform. to screen
print(g, 'Scanning Completed in: ', total)




