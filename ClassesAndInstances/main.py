class Pegawai:

    def __init__(self, nama, email, gaji):
        self.namaPegawai = nama
        self.emailPegawai = email + 'gmail.com'
        self.gajiPegawai = gaji

    # nama dari method tidak boleh sama dengan property
    # contoh : method gajiPegawai()
    def gajiPegawaiCalculate(self):
        # parameter self pada method merupakan hal yang sama dengan
        # Pegawai.gajiPegawai(namaInstance)
        self.gajiPegawai = self.gajiPegawai * 30
        return self.gajiPegawai

    # def gajiPegawaiCalculate():
        #ini merupakan contoh dimana method yang tidak disarankan
        # karena tidak menempatkan self di parameternya.
        # dan jika itu terjadi maka program tidak akan membaca instance yang dipilih
        

# ini merupakan instance dari Class Pegawai
pegawai = Pegawai('Mohamad Fahmi','email.com',2000)
pegawai2 = Pegawai('Solihin','yahoo.com',2001)


# tiap instance akan memiliki value property yang berbeda 
# hal ini karena dia dibentuk didalam waktu yang berbeda
print(pegawai.namaPegawai)
print(pegawai2.namaPegawai)

# gajiPegawai merupakan method itulah mengapa memiliki tanda '()'
print(pegawai.gajiPegawaiCalculate())
print(pegawai2.gajiPegawaiCalculate())