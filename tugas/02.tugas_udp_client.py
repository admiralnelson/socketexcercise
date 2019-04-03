# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
IP = "localhost"

# definisikan target port number server yang akan dituju
PORT = 1257

PESAN = "A rest, if you will, mein Kaiser."

print ("target IP:", IP)
print ("target port:", PORT)
print ("pesan:", PESAN)

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan loop 10 kali
for x in range (10):
    # definisikan pesan yang akan dikirim
    sock.sendto(bytearray(PESAN, "ascii"), (IP, PORT))
    
    # kirim pesan    
    