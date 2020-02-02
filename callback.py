import json
import copy
from datetime import datetime

import connection
from utility import getHwAddr

def callback(bt_addr, rssi, packet, additional_info):
    #print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    if hasattr(packet, 'voltage'):
       initialize_data = copy.deepcopy(connection.settings.EDISTONE_FORMAT)

       initialize_data["timestamp"] = datetime.today().strftime("%Y-%m-%d %H:%m-%s")
       initialize_data["edgemac"] = getHwAddr('enp1s0')
       initialize_data["mac_address"] = bt_addr
       initialize_data["uid_namespace"] = additional_info["namespace"]
       initialize_data["rssi"] = rssi
       initialize_data["temperature"] = packet.temperature_fixed_point
       initialize_data["voltage"] = packet.voltage
       
       client = connection.connect_to_message_broker() 
       client.publish("topic/gen", json.dumps(initialize_data))       
       client.disconnect()
