# -*- coding: utf-8 -*-

import requests
from tkinter import*
from PIL import Image, ImageTk
from bs4 import BeautifulSoup

class HavaDurumu:
    def __init__(self, url, header):
        self.url = url
        self.header = header
        self.r = requests.get(self.url, headers={"User-Agent":self.header})
        self.soup = BeautifulSoup(self.r.content, "html.parser")

        self.ceviri = {
            "Tonight":"gece",
            "Today":"gunduz"
        }
        self.simgeler = {
            "gece": ImageTk.PhotoImage(Image.open("night.png")),
            "gunduz": ImageTk.PhotoImage(Image.open("day.png"))
        }

    def isim(self):
        self.isim = self.soup.find("div", attrs={"class":"wr-c-location"}).h1.text
        self.ismiDuzenle = str(self.isim).split()[0]
        return self.ismiDuzenle

    def tarih(self):
        self.tarih = self.soup.find("div", attrs={"class":"wr-day__title wr-js-day-content-title"}).span.text
        self.tarihiDuzenle = str(self.tarih).split()[0]
        for i in self.ceviri.keys():
            if i == self.tarihiDuzenle:
                self.tarihiDuzenle = self.ceviri.get(i)
                self.simge()
                return self.tarihiDuzenle

    def simge(self):
        for x in self.simgeler.keys():
            if x == self.tarihiDuzenle:
                return self.simgeler.get(x)

    def sicaklik(self):
        self.sicaklik = self.soup.find("span", attrs={"class":"wr-day-temperature__high-value"}).select("span > span")[0].text
        return self.sicaklik[:3]

if __name__ == '__main__':
    ornekle = HavaDurumu()