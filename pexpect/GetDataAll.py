# Python script to get data from multiple devices
# Usage:
# python GetDataAll.py
import subprocess
# list of devices
devices = [
  "80:AD:16:87:8F:AE",  # device 01
   ]
for x in range(0,len(devices)):
  cmd = "python GetData.py " + devices[x]
  subprocess.call(cmd, shell=True)
print("finished all devices!")
