from Apoteker import Apoteker
from Pegawai import Pegawai
from Dokter import Dokter

apk1 = Apoteker('Solihin','Sesuatu',20000,'Meracik Obat')

dkt = Dokter('Dr.Mamang','wow',90000,['Ahli Mata','Ahli Hidung'])

print(apk1.naikJabatanPegawai())

# untuk mengetahui apakah sebuah instance merupakan dari kelas yang dimaksud
print(isinstance(dkt, Pegawai))
print(isinstance(apk1, Dokter))

# untuk mengetahui apakah kelas tersebut merupakan turunannya.
print(issubclass(Dokter, Pegawai))
print(issubclass(Dokter, Apoteker))

print(dkt.namaPegawai)
dkt.addSpesialis('Ahli Organ')
dkt.printSpesialis()
print("=============")
dkt.removeSpeasialis('Ahli Mata')
dkt.printSpesialis()