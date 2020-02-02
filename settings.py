BROKER = 1 # 1 for mqtt and 2 for other mqtt

#EDISTONE_FORMAT = {"timestamp":"","mac_address":"","uid_namespace":"","edge_mac":"","latitude":"","longitude":"","rssi":"","temperature":"","voltage":""}
from collections import OrderedDict
EDISTONE_FORMAT=OrderedDict()
EDISTONE_FORMAT["timestamp"] =""
EDISTONE_FORMAT["edgemac"] =""
EDISTONE_FORMAT["latitude"] =""
EDISTONE_FORMAT["longitude"] =""
EDISTONE_FORMAT["mac_address"] =""
EDISTONE_FORMAT["rssi"] =""
EDISTONE_FORMAT["battery"] =""
EDISTONE_FORMAT["temperature"] =""
EDISTONE_FORMAT["humidity"] =""
EDISTONE_FORMAT["voltage"] =""
EDISTONE_FORMAT["uid_namespace"] =""