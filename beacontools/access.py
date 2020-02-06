from binascii import hexlify
import array
import htoi

def acceess(packet):
    #print("Packet>>> ", packet)
    #print(len(packet))
    #ex = "0201060303aafe1316aafe807720003c00c4ffdcfff0fb0cfc0300"
    #print(len(ex))
    packet = array.array('B', packet)
    #packet.reverse()
    hexi = hexlify(packet.tostring())
    #print("hexi>>> ", hexi)
    #print(len(hexi))
    #print(hexi[46:52])
    if hexi[46:52] == "aafe80":
        #print(hexi)
        Counter = hexi[52:54]
        Data = hexi[54:82]
        print("Data>>>",Data)
        #print(len(Data))
        Xmin = Data[2:4]+Data[0:2]
        Xmax = Data[6:8]+Data[4:6]
        Ymin = Data[10:12]+Data[8:10]
        Ymax = Data[14:16]+Data[12:14]
        Zmin = Data[18:20]+Data[16:18]
        Zmax = Data[22:24]+Data[20:22]
        Rms = Data[26:]+Data[24:26]
        
        xmin = htoi.s16(int(Xmin,16))
        xmax = htoi.s16(int(Xmax,16))
        
        ymin = htoi.s16(int(Ymin,16))
        ymax = htoi.s16(int(Ymax,16))
        
        zmin = htoi.s16(int(Zmin,16))
        zmax = htoi.s16(int(Zmax,16))
        rms = htoi.s16(int(Rms,16))
        print("Counter>>", Counter)
        print("Xmin>>", xmin," --- Xmax>>", xmax)
        print("Ymin>>", ymin," --- Ymax>>", ymax)
        print("Zmin>>", zmin," --- Zmax>>", zmax)
        print("RMS>>", rms)
        print("=================================")
