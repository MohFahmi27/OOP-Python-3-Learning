class Pegawai:
    kenaikanGaji = float(1.05)

    def __init__(self, nama, email, gaji):
        self.namaPegawai = nama
        self.emailPegawai = email + 'gmail.com'
        self.gajiPegawai = gaji

    def gajiCalculateMontly(self):
        self.gajiPegawai = self.gajiPegawai * 30
        return self.gajiPegawai
    
    def naikJabatanPegawai(self):
        self.gajiPegawai = float(self.gajiPegawai + self.kenaikanGaji)
        return self.gajiPegawai

    # ini merupakan sebuah dekorator yang dimana method 
    # tersebut akan dapat dipanggil dengan nama kelas 
    # ini juga dapat dibilang dengan alternatif konstruktor
    @classmethod
    def setKenaikanGaji(cls, besar):
        cls.kenaikanGaji = besar

    # penggunaan static method digunakan apabila sebuah method
    # tidak perlu mengakses sebuah instance atau kelasnya
    @staticmethod
    def cekHariKerja(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# ini merupakan classmethod 
Pegawai.setKenaikanGaji(19)
print(Pegawai.kenaikanGaji)
pegawai = Pegawai('Mohamad Fahmi','email.com',2000)
pegawai2 = Pegawai('Solihin','yahoo.com',2001)

# berikut merupakan contoh dari penggunaan classmethod
print(pegawai2.kenaikanGaji)
pegawai2.setKenaikanGaji(20)
print(pegawai2.kenaikanGaji)

# berikut contoh penggunaan staticmethod
import datetime

myDate = datetime.date(2020, 3, 23)
print(Pegawai.cekHariKerja(myDate))