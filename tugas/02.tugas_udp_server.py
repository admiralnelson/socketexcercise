# import library socket karena akan menggunakan IPC socket
import socket

BUFFER_SIZE = 1024

# definisikan alamat IP bind dari server
IP = "localhost"

# definisikan port number untuk bind dari server
PORT = 1257

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan bind
sock.bind((IP, PORT))

# loop forever
while True:
    # terima pesan dari client
    data, ip = sock.recvfrom(BUFFER_SIZE)
    
    # menampilkan hasil pesan dari client
    print (data," message " , ip)
    
    
