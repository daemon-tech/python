#python3.8
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate a host name to IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

#Add banner
print("*"*50)
print("Scanning target {}".format("target"))
print("Time started: "+str(datetime.now()))
print("*"*50)

try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(.1) #float
		result = s.connect_ex((target, port)) #returns error
		print("Checking Port: {}".format(port))
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting script.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()