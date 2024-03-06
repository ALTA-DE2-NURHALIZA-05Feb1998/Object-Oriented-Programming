# tulis solusi code disini
class ongkoskirim :
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang=panjang
        self.lebar=lebar
        self.tinggi=tinggi
        self.berat=berat
    def ongkos(self):
        if self.panjang * self.lebar * self.tinggi >=50 or abs(self.berat)==1 :
            return 5000
        else :
            return "0"
ongkos_kirim=ongkoskirim(5, 2, 4, 1)
print(f' harga pengiriman barang adalah : {ongkos_kirim.ongkos()}')