from Pegawai import Pegawai

class Dokter(Pegawai):

    # contoh jika sebuah property menggunakan list string atau list objek
    def __init__(self, nama, email, gaji, spesialis = []):
        # function super() digunakan untuk mengoper property 
        # nama, email, dan gaji ke parent kelas
        # hal ini untuk tidak mengulangi logict yang ada di konstruktor
        # yang ada di parent kelas
        super().__init__(nama, email, gaji)
        self.spesialis = spesialis

    def addSpesialis(self, spesialisAdd):
        if spesialisAdd not in self.spesialis:
            self.spesialis.append(spesialisAdd)

    # digunakan untuk menghapus elemen yang ada di spesialis
    def removeSpeasialis(self, spesialisName):
        if spesialisName in self.spesialis:
            self.spesialis.remove(spesialisName)

    # digunakan untuk mencetak semua elemen yang ada di list spesialis
    def printSpesialis(self):
        for i in range(len(self.spesialis)):
            print('===> ', self.spesialis[i])
        # jika ingin menggunakan ouput berupa objek
        # for i in self.spesialis:
        #  print('===>', i.spesialis)