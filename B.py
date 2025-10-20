class Dosen: 
    def __init__(self, nidn, nama): 
        self._nidn = None 
        self.nama = nama 
        self.nidn = nidn
    
    @property 
    def nidn(self): 
        return self._nidn
    
    @nidn.setter 
    def nidn(self, value): 
        if not (value.isdigit() and len(value) == 10): 
            raise ValueError("NIDN harus 9 digit angka.") 
        self._nidn = value 
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIDN: {self.nidn}")

m = Dosen("123456789", "Lendra")
print(m.nidn)
