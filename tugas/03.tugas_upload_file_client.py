# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
IP = "localhost"

# definisikan port number proses di server
PORT = 1257

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 1024

# buat socket (apakah bertipe UDP atau TCP?)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python

f = open("file_diupload.txt", "rb")
try:
    # baca file tersebut sebesar buffer 
    i = 0
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while True:
        # kirim hasil pembacaan file
        data = f.read(BUFFER_SIZE)
        sock.sendto(data, (IP, PORT))
        i += BUFFER_SIZE
        print("terkirim ", i, " B")
        # baca sisa file hingga EOF
        if data == b'' : break
        #print(byte)
finally:
    print ("end sending")
    f.close()
    # tutup file jika semua file telah  dibaca
    sock.close()

# tutup koneksi setelah file terkirim
