# tulis solusi code disini
#menghitung volume kubus
class kubus:
    def __init__(self, sisi):
        self.sisi=sisi
    
    def volume_kubus(self):
        return self.sisi*self.sisi*self.sisi
class balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang=panjang
        self.lebar=lebar
        self.tinggi=tinggi
    def volume_balok(self):
        return self.panjang*self.lebar*self.tinggi
class tabung:
    def __init__(self, jari_jari, tinggi):
        self.phi = 3.14285714286
        self.jari_jari=jari_jari
        self.tinggi=tinggi
    def volume_tabung(self):
        return self.phi * (self.jari_jari**2) * self.tinggi
#-------------menampilkan hasil--------
kubus = kubus(10)
print(f'volume kubus adalah : {kubus.volume_kubus()}')

balok=balok(3,6,10)
print(f'volume balok adalah : {balok.volume_balok()}')

tabung=tabung(7,10)
print(f'volume tabung adalah : {tabung.volume_tabung()}')