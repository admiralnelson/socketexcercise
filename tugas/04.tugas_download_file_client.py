# import library socket karena menggunakan IPC socket
import socket
import os

# definisikan IP server tujuan file akan diupload
IP = "localhost"

# definisikan port number proses di server
PORT = 1257

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 1024

# buat socket (apakah bertipe UDP atau TCP?)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# lakukan koneksi ke server


# buka file bernama "hasil_download.txt bertipe byte
f = open("hasil_download.txt", "wb") 
# masih hard code, file harus ada dalam folder yang sama dengan script python
# loop forever
try:
    while True:
        # terima pesan dari client
        sock.settimeout(10)
        data, addr = sock.recvfrom(BUFFER_SIZE)
        # berhenti jika sudah tidak ada pesan yang dikirim
        f.write(data)
        # tulis pesan yang diterima dari client ke file kita (result.txt)
except:    
    # tutup file_hasil_download.txt    
    f.close()
    downloadedFile = os.stat("hasil_download.txt")
    originalFile = os.stat("file_didownload.txt")
    print(" file download ", downloadedFile.st_size, " B ", " file ori ", originalFile.st_size, " B ", " sama? ", downloadedFile.st_size == originalFile.st_size)

    #tutup socket
    sock.close()
