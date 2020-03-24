from abc import ABC, abstractmethod

# setiap kelas abstract harus inheritance terhadap module ABC
# yang dimana module tersebut akan membuat kelas Shape tidak dapat dibuat instance
class Shape(ABC):

    # dekorator ini dapat membuat method ini harus diimplementasikan
    # terhadap sub-classnya. jika tidak akan menghasilkan error
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod    
    def keliling(self):
        pass