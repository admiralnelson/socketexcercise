# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
IP = "localhost"

# definisikan port number binding  yang akan digunakan 
PORT = 1257

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# buat socket bertipe TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
sock.bind((IP, PORT))

# server akan listen menunggu hingga ada koneksi dari client
sock.listen(1)
conn, addr = sock.accept()
print("Connection addr ", addr)
# lakukan loop forever
while True:
	# menerima koneksi
    data = conn.recv(BUFFER_SIZE)

	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
	# menerima data berdasarkan ukuran buffer
	# menampilkan pesan yang diterima oleh server menggunakan print
    print("data ", data, " from ", addr)

	# mengirim kembali data yang diterima dari client kepada client
    conn.send(bytearray("I need to grab an axe...", "ascii"))    

# tutup koneksi	
conn.close()
