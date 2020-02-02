import bluetooth

target_name = "Redmi Note 5"
target_address = None

from beacontools import parse_packet

# tlm_packet = b"\x02\x01\x06\x03\x03\xaa\xfe\x11\x16\xaa\xfe\x20\x00\x0b\x18\x13\x00\x00\x00" \
#              b"\x14\x67\x00\x00\x2a\xc4\xe4"
# tlm_frame = parse_packet(tlm_packet)
# print("Voltage: %d mV" % tlm_frame.voltage)
# print("Temperature: %d C" % tlm_frame.temperature)
# print("Advertising count: %d" % tlm_frame.advertising_count)
# print("Seconds since boot: %d" % tlm_frame.seconds_since_boot)


nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    #if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        print ">>>>>>>>>>>>>>>>>",target_address
    #    break

# if target_address is not None:
#     print "found target bluetooth device with address ", target_address
# else:
#     print "could not find target bluetooth device nearby"