from Pegawai import Pegawai

# kelas ini inheritance terhadao kelas Pegawai
class Apoteker(Pegawai):

    # kelas variable yang ada di parent kelas 
    # dapat diganti dengan mudah
    kenaikanGaji = 1.08

    def __init__(self, nama, email, gaji, keahlian):
        # function super() digunakan untuk mengoper property 
        # nama, email, dan gaji ke parent kelas
        # hal ini untuk tidak mengulangi logict yang ada di konstruktor
        # yang ada di parent kelas
        super().__init__(nama, email, gaji)
        self.keahlian = keahlian