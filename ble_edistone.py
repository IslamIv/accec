import time
from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneFilter, EddystoneUIDFrame
from callback import callback

scanner = BeaconScanner(callback, 
    device_filter=EddystoneFilter(namespace="8b9cc73c3ae747ef65bc"),
    packet_filter=[EddystoneTLMFrame, EddystoneUIDFrame]
)
scanner.start()

#time.sleep(10)
#scanner.stop()