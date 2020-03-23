class Pegawai:
    kenaikanGaji = 1.05

    def __init__(self, nama, email, gaji):
        self.namaPegawai = nama
        self.emailPegawai = email + 'gmail.com'
        self.gajiPegawai = gaji        

    def gajiCalculateMontly(self):
        self.gajiPegawai = self.gajiPegawai * 30
        return self.gajiPegawai
    
    def naikJabatanPegawai(self):
        self.gajiPegawai = float(self.gajiPegawai * self.kenaikanGaji)
        return self.gajiPegawai