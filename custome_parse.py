# -*- coding: utf-8 -*-
from beacontools import parse_packet

tlm_packet = b"\x02\x01\x03\x01\xb9\xa4\xa9\xc8\xdb\xcc\x1e\x02\x01\x06\x1a\xffL\x00\x02\x15\xf7\x82m\xa6O\xa2N\x98\x80$\xbc[q\xe0\x89>zY\xab\xf5\xb3\xbf"
tlm_frame = parse_packet(tlm_packet)

print("tlm_frame",tlm_frame)
print("Voltage: %d mV" % tlm_frame.voltage)
print("Temperature: %d °C" % tlm_frame.temperature)
print("Advertising count: %d" % tlm_frame.advertising_count)
print("Seconds since boot: %d" % tlm_frame.seconds_since_boot)