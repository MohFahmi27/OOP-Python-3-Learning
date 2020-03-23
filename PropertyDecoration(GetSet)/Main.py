from Pegawai import Pegawai

pegawai1 = Pegawai('Fahmi Wal','sesuatu@gamil.com',10000)

# berikut ini merupakan penggunaan getter pada kelas Pegawai
print(pegawai1.namaPegawai)

# berikut ini penggunaan setiap setter pada kelas Pegawai
pegawai1.gajiPegawai = 10_000_000
pegawai1.emailPegawai = 'Hal.negatif@gmail.com'
pegawai1.namaPegawai = 'Mohammad Fahmi'

print(pegawai1.__str__())