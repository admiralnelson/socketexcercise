# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
IP = "localhost"

# definisikan port dari server yang akan terhubung
PORT = 1257

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# definisikan pesan yang akan disampaikan
MESSAGE = "Wood stocks are too low, Sire."

# buat socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
sock.connect((IP, PORT))

# kirim pesan ke server
sock.send(bytearray(MESSAGE, "ascii"))

# terima pesan dari server
data = sock.recv(BUFFER_SIZE)

# tampilkan pesan/reply dari server
print(data)

# tutup koneksi
sock.close()

