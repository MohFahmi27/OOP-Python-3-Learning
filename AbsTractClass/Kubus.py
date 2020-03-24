from Shape import Shape

class Kubus(Shape):

    def __init__(self,side):
        self.side = side

    # proses overriding dari abstract kelas
    # proses ini wajib dilakukan jika inheritance dengan kelas abstract
    def luas(self):
        return 6*(self.side**2)
    
    def keliling(self):
        return 12*self.side

kubus = Kubus(10)
print(kubus.luas())
print(kubus.keliling())