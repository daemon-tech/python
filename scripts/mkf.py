#mkf.py by OSzeroday
import os
import sys
import time as t
from datetime import datetime

#A small annoying py script for creating dir in current path

os.system("clear")
path = os.getcwd()
print("-"*100)
print("The current directory is %s" % path)

datetime_now = datetime.now()
start_time = datetime_now.strftime("%H:%M:%S")
t1 = datetime.now()

print("Script starting at {}".format(start_time))
print("-"*100)
t.sleep(5)

try:
	#while True:
	for i in range(0, 1000+1):
		directory_path_name = "{}/{}".format(path, i)
		os.makedirs(directory_path_name)
		print("{}: {} Successfully generated".format(i, directory_path_name))
	datetime_now = datetime.now()
	end_time = datetime_now.strftime("%H:%M:%S")
	t2 = datetime.now()
	time_difference = t2 - t1
	print("Script ended at {}     Total time difference: {}".format(end_time, time_difference))

except OSError:
	print("Creation of directory {} failed".format(path))

except KeyboardInterrupt:
	print("Pressed Ctrl+C, exiting script now!")
	sys.exit()

else:
    print("No exception occurred")

