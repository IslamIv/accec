import json
import copy
from datetime import datetime
import os

import connection
from utility import getHwAddr
script_dir = os.path.dirname(__file__)
#print("DIR>>>", script_dir)
path = script_dir+"/beacontools/tx1.txt"
def callback(bt_addr, rssi, packet, additional_info):
    #print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    if hasattr(packet, 'voltage'):
       initialize_data = copy.deepcopy(connection.settings.EDISTONE_FORMAT)
       #print("from callback", acc_data)
       initialize_data["timestamp"] = datetime.today().strftime("%Y-%m-%d %H:%m-%s")
       initialize_data["edgemac"] = getHwAddr('enp1s0')
       initialize_data["mac_address"] = bt_addr
       initialize_data["uid_namespace"] = additional_info["namespace"]
       initialize_data["rssi"] = rssi
       initialize_data["temperature"] = packet.temperature_fixed_point
       initialize_data["voltage"] = packet.voltage
       acc_data = json.load(open(path))
       #print("CALP>>", acc_data)
       initialize_data["X_min"] =acc_data["xmin"]
       initialize_data["X_max"] =acc_data["xmax"]
       initialize_data["Y_min"] =acc_data["ymin"]
       initialize_data["Y_max"] =acc_data["ymax"]
       initialize_data["Z_min"] =acc_data["zmin"]
       initialize_data["Z_max"] =acc_data["zmax"]
       initialize_data["RMS"] = acc_data["rms"]
       print(json.dumps(initialize_data))
       #client = connection.connect_to_message_broker() 
       #client.publish("topic/gen", json.dumps(initialize_data))       
       #client.disconnect()
