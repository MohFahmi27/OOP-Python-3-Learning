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
    
    # ini merupakan contoh dari dunder biasanya method dunder (double underscore) yang paling banyak digunakan adalah 
    # dunder biasanya digunakan untuk overloading function yang sudah built-in didalam python.
    # method __init__, __str__, __add__ dan __repr__ 
    # __str__ digunakan untuk membuat objek untuk bisa dibaca oleh user
    def __str__(self):
        return "Nama Pegawai : {} \nEmail : {}\nGajiPegawai : {}".format(self.namaPegawai,self.emailPegawai,self.gajiPegawai)

    # __repr__ digunakan untuk membuat objek untuk bisa dibaca oleh developer lain,
    # maka dari itu ouput dari __repr__ dapat berupa kodingan dari objeknya sendiri.
    def __repr__(self):
        return "Pegawai('{}','{}',{})".format(self.namaPegawai,self.emailPegawai,self.gajiPegawai)

    # digunakan untuk menembahkan gaji dari 2 instance
    # disini parameternya menerima dua instance dari kelas Pegawai 
    # dan menambahkan jumlah gaji dari mereka.
    def __add__(self, other):
        return self.gajiPegawai + other.gajiPegawai

    # digunakan untuk mengetahui panjang dari karakter namaPegawai
    def __len__(self):
        return len(self.namaPegawai)

pegawai1 = Pegawai("Moahmmad", "Sesuatu", 2000)
pegawai2 = Pegawai("Solihin", "Sesuatuhal", 2001)


print(Pegawai.__add__(pegawai1, pegawai2))
print(pegawai1.__len__())
print(pegawai1.__str__())
print(pegawai1.__repr__())