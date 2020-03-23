class Pegawai:

    # ini merupakan contoh dari varible class:
    # misal kenaikan gaji pegawai adalah tiap naik jabatan
    kenaikanGaji = float(1.05)
    jumPegawai = 0


    def __init__(self, nama, email, gaji):
        self.namaPegawai = nama
        self.emailPegawai = email + 'gmail.com'
        self.gajiPegawai = gaji

        # ini merupakan contoh dari class variable yang statis dengan kelasnya
        Pegawai.jumPegawai += 1
        # setiap kali instance dibuat maka akan menambahkan variable jumPegawai

    def gajiCalculateMontly(self):
        self.gajiPegawai = self.gajiPegawai * 30
        return self.gajiPegawai
    
    def naikJabatanPegawai(self):
        # menggunakan self.kenaikanGaji dilakukan karena jika 
        # salah satu pegawai memiliki kenaikan yang berbeda maka 
        # akan mengecek variable kelas dari sebuah instance dan jika tidak 
        # akan mengecek variable kelas default contoh disini adalah Pegawai.kenaikanGaji
        self.gajiPegawai = float(self.gajiPegawai + self.kenaikanGaji)
        return self.gajiPegawai
        
print(Pegawai.jumPegawai)
pegawai = Pegawai('Mohamad Fahmi','email.com',2000)
pegawai2 = Pegawai('Solihin','yahoo.com',2001)
print(Pegawai.jumPegawai)


print(pegawai.kenaikanGaji)
print(pegawai2.kenaikanGaji)
pegawai.kenaikanGaji = 1.09
print(pegawai.kenaikanGaji)
print(pegawai2.kenaikanGaji)

print(pegawai.naikJabatanPegawai())