class Pegawai:

    def __init__(self, nama, email, gaji):
        self.__namaPegawai = nama
        self.__emailPegawai = email
        self.__gajiPegawai = gaji

    @property
    def namaPegawai(self):
        return self.__namaPegawai

    @namaPegawai.setter
    def namaPegawai(self, nama):
        self.__namaPegawai = nama

    @property
    def emailPegawai(self):
        return self.__emailPegawai
    
    @emailPegawai.setter
    def emailPegawai(self, email):
        self.__emailPegawai = email

    @property
    def gajiPegawai(self):
        return self.__gajiPegawai
    
    @gajiPegawai.setter
    def gajiPegawai(self, gaji):
        self.__gajiPegawai = gaji

    def __str__(self):
        return "Nama Pegawai : {} \nEmail : {}\nGajiPegawai : {}".format(self.namaPegawai,self.emailPegawai,self.gajiPegawai)