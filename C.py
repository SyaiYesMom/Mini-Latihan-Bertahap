class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas


class KelasKuliah:
    def __init__(self, kode_kelas, ruang):
        self.kode_kelas = kode_kelas
        self.ruang = ruang
        self.peserta = []

    def tambah_peserta(self, nama_mahasiswa):
        if len(self.peserta) < self.ruang.kapasitas:
            self.peserta.append(nama_mahasiswa)
        else:
            print(f"Tidak bisa menambahkan {nama_mahasiswa}, kapasitas penuh!")

    def info(self):
        print(f"Kelas {self.kode_kelas} ({len(self.peserta)}/{self.ruang.kapasitas})")
        print("Peserta : -", "          - ".join(self.peserta))


ruang1 = Ruang("R101", 3)
kelas1 = KelasKuliah("TI-23A5", ruang1)
kelas1.tambah_peserta("Gigieh\n")
kelas1.tambah_peserta("Luthfi\n")
kelas1.tambah_peserta("Lendraa\n")
kelas1.tambah_peserta("Irfan\n")
kelas1.info()
