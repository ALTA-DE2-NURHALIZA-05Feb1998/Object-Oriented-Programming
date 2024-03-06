# tulis solusi code disini
class penjumlahan:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def jumlah(self):
        return self.a+self.b
class pengurangan:
    def __init__(self, a, b):
        self.a=a
        self.b=b 
    def kurang(self):
        return self.a-self.b 
class perkalian:
    def __init__(self, a, b):
        self.a=a
        self.b=b 
    def kali(self):
        return self.a*self.b 
class pembagian:
    def __init__(self, a, b):
        self.a=a
        self.b=b 
    def bagi(self):
        return self.a/self.b 
#------------tampilkan hasil------------
penjumlahan = penjumlahan(3,4)
print(f'hasil tambah 3+4 adalah : {penjumlahan.jumlah()}')

pengurangan=pengurangan(15,4)
print(f'hasil kurang 15-4 adalah : {pengurangan.kurang()}')

perkalian=perkalian(10,10)
print(f'hasil kali 10x10 adalah : {perkalian.kali()}')

pembagian=pembagian(12,3)
print(f'hasil bagi 12/3 adalah : {pembagian.bagi()}')

    
