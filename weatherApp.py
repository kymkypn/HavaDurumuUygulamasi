# -*- coding: utf-8 -*-

from tkinter import*
from weather import HavaDurumu


class Uygulama:
    def __init__(self):
        pencere.title("Guncel Hava Durumu")
        pencere.iconbitmap("weather.ico")
        pencere.geometry("800x600+400+100")
        self.header = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"

        self.sehirLinkler = {"Ankara":"https://www.bbc.com/weather/323786",
                             "Istanbul":"https://www.bbc.com/weather/745044",
                             "Izmir":"https://www.bbc.com/weather/311046",
                             "Bursa":"https://www.bbc.com/weather/750269",
                             "-"*20:"",
                             "Washington":"https://www.bbc.com/weather/4140963",
                             "Paris":"https://www.bbc.com/weather/2988507",
                             "Roma":"https://www.bbc.com/weather/6299616",
                             "Londra":"https://www.bbc.com/weather/2643743",
                             "Viyana":"https://www.bbc.com/weather/2761369",
                             }

        self.ekranAraclari()

    # Listbox ogelerinden secilen ogeyi
    # donduruyoruz.
    def secildi(self):
        self.secilen = self.sehirlerBox.curselection()
        return self.sehirlerBox.get(self.secilen)

    def goster(self):
        self.secildi()

        for x in self.sehirLinkler.keys():
            if x == self.secildi():
                self.sehir = HavaDurumu(self.sehirLinkler.get(x), self.header)
                self.durum = self.sehir.isim(), self.sehir.tarih(), self.sehir.sicaklik()

        self.simgeGoster = Label(image=self.sehir.simge()).place(relx=0.7, rely=0.2)

        self.havaDurumunuGoster.delete(0, END)
        self.havaDurumunuGoster.insert(0, self.durum)

    def ekranAraclari(self):
        # Bir Listbox widget (Pencere aracı) tanımlıyoruz.
        # Yukarıda olusturdugumuz sozlugun key lerini
        # yani sehir isimlerini Listbox'ımıza bir
        # for dongusu aracılıgıyla ekliyoruz.
        self.sehirlerBox = Listbox(font="Helvetica 15", selectmode=SINGLE)
        self.sehirlerBox.pack(side=LEFT)
        for i in self.sehirLinkler.keys():
            self.sehirlerBox.insert(END, i)

        # Secilen sehrin hava durumunu gormek icin
        # bir buton olusturuyoruz. command(komut) parametresine
        # arguman olarak goster metodunu veriyoruz. Bu butona
        # tiklandıgında goster metodu calisacak.
        self.havayiOgren = Button(text="Hava Durumu", font="Helvetica 30", command=self.goster)
        self.havayiOgren.place(relx=0.3, rely=0.0)

        self.havaDurumunuGoster = Entry(width=25, font="Helvetica 20")
        self.havaDurumunuGoster.place(relx=0.5, rely=0.4)

pencere = Tk()
uyg = Uygulama()
mainloop()
