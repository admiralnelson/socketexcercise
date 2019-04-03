# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
IP = "localhost"

# definisikan port untuk binding
PORT = 1257

# definisikan ukuran buffer untuk menerima pesan
BUFFER_SIZE = 1024

# buat socket (bertipe UDP atau TCP?)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan binding ke IP dan port
# lakukan listen

#  siap menerima koneksi

# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python

try:
    # baca file tersebut sebesar buffer 
    f = open("file_didownload.txt", "rb")
    data = f.read(BUFFER_SIZE)
    i = 0
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while data != b'':
        # kirim hasil pembacaan file dari server ke client
        if(sock.sendto(bytearray(data), (IP, PORT))):
            i += BUFFER_SIZE
            print("terkirim ", i, " B")
            data = f.read(BUFFER_SIZE)
        # baca sisa file hingga EOF
        
        
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()
    sock.close()

# tutup socket


# tutup koneksi
