class Dosen:
    def __init__(self, nidn, nama):
        self.nidn = nidn
        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")


dosen1 = Dosen("1234567890", "Triyono")
dosen2 = Dosen("0987654321", "Syailendra")

dosen1.info()
dosen2.info()
