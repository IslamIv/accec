from binascii import hexlify
import array

def acceess(packet):
    print("Packet>>> ", packet)
    print(len(packet))
    #ex = "0201060303aafe1316aafe807720003c00c4ffdcfff0fb0cfc0300"
    #print(len(ex))
    packet = array.array('B', packet)
    packet.reverse()
    hexi = hexlify(packet.tostring())
    print("hexi>>> ", hexi)
    print(len(hexi))
