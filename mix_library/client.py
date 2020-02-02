from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("80:AD:16:87:8F:AE", 3))

client_socket.send("Hello World")

print "Finished"

client_socket.close()