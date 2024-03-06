# tulis solusi code disini
import math
#menghitung persegi
class persegi :
    def __init__(self, sisi):
        self.sisi=sisi
    def hitung_luas_dan_keliling(self):
        luas=self.sisi*self.sisi
        keliling=4*self.sisi
        return luas, keliling

##menghitung segitiga
class segitiga :
    def __init__(self, alas,tinggi):
        self.alas=alas
        self.tinggi=tinggi
    def hitung_segitiga(self):
        luas = 0.5 * self.alas * self.tinggi
        keliling =self.alas + self.tinggi + math.sqrt(self.alas*self.alas+self.tinggi*self.tinggi)
        return luas, keliling

#menghitung persegi panjang
class persegi_panjang :
    def __init__(self, panjang, lebar):
        self.panjang=panjang
        self.lebar=lebar
    def hitung_persegi_panjang(self):
        luas = self.panjang * self.lebar
        keliling= 2*self.panjang + 2*self.lebar
        return luas, keliling
    
#------------menampilkan hasil------------
persegi=persegi(4)
luas, keliling = persegi.hitung_luas_dan_keliling()
print(f"luas persegi adalah : {luas}, keliling persegi adalah : {keliling}")

segitiga=segitiga(3,4)
luas, keliling = segitiga.hitung_segitiga()
print(f"luas segitiga adalah :{luas}, keliling segitiga adalah {keliling}")

persegi_panjang =persegi_panjang(7,8)
luas, keliling = persegi_panjang.hitung_persegi_panjang()
print(f"luas persegi panjang adalah {luas}, keliling persegi panjang adalah {keliling}")

