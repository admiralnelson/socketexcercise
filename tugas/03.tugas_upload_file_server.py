# import library socket karena menggunakan IPC socket
import socket
import os
# definisikan IP untuk binding
IP = "localhost"

# definisikan port untuk binding
PORT = 1257

# definisikan ukuran buffer untuk menerima pesan
BUFFER_SIZE = 1024

# buat socket (bertipe UDP atau TCP?)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan binding ke IP dan port
sock.bind((IP, PORT))

# lakukan listen

#  siap menerima koneksi


# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
f = open("hasil_diupload.txt", "wb") 

# loop forever
i = 0
while True:
    # terima pesan dari client
    data, addr = sock.recvfrom(BUFFER_SIZE)
    i += BUFFER_SIZE
    print ('Connection address:', addr, " downloading: ", i , " B")
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    f.write(data)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if data == b'': break
    
# tutup file result.txt   
f.close()
sock.close()

uploadedFile = os.stat("hasil_diupload.txt")
originalFile = os.stat("file_diupload.txt")
print(" file upload ", uploadedFile.st_size, " B ", " file ori ", originalFile.st_size, " B ", " sama? ", uploadedFile.st_size == originalFile.st_size)

#tutup socket


# tutup koneksi

