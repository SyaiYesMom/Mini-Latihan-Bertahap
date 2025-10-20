class Dosen:
    def __init__(self, nidn, nama):
        # Validasi NIDN harus 10 digit angka
        if not (nidn.isdigit() and len(nidn) == 10):
            raise ValueError("❌ NIDN harus terdiri dari 10 digit angka.")
        self.nidn = nidn
        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")


class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas


class KelasKuliah:
    def __init__(self, kode_kelas, ruang):
        self.kode_kelas = kode_kelas
        self.ruang = ruang
        self.mahasiswa = []

    def tambah_mahasiswa(self, nama):
        if len(self.mahasiswa) < self.ruang.kapasitas:
            self.mahasiswa.append(nama)
        else:
            print(f"⚠️ Tidak dapat menambah {nama}. Ruang {self.ruang.kode} sudah penuh!")

    def tampilkan_mahasiswa(self):
        print(f"\nDaftar Mahasiswa di {self.kode_kelas}:")
        for m in self.mahasiswa:
            print(f"- {m}")

    def tampilkan_mahasiswa_awal_DE(self):
        print("\nMahasiswa dengan nama diawali huruf D atau E:")
        for m in self.mahasiswa:
            if m[0].upper() in ['D', 'E']:
                print(f"- {m}")


# --- PROGRAM UTAMA ---
try:
    dosen1 = Dosen("1234567890", "Triyono")
    dosen2 = Dosen("0987654321", "Syailendra")
    dosen1.info()
    dosen2.info()
except ValueError as e:
    print(e)

# Buat ruang kuliah dengan kapasitas 10
ruangA = Ruang("R101", 10)

# Buat kelas kuliah
kelas = KelasKuliah("IF-1", ruangA)

# Tambah beberapa mahasiswa ke kelas
daftar_mahasiswa = [
    "Hafan", "Eka", "Aziz", "Irfan", "Minan", "Savina", "Trafika", "Lendra",
    "Luthfi", "Fitra", "Dhiwa", "Kahfi", "Desta", "Viqi", "Arsa", "Domingos",
    "Pratama", "Gigieh", "Faris", "Ridho", "Adit", "Bima", "Fahryan", "Nabil",
    "Najib", "Nathan", "Raihan", "Raka", "Rofi"
]

for nama in daftar_mahasiswa:
    kelas.tambah_mahasiswa(nama)

# Tampilkan daftar mahasiswa dan filter D/E
kelas.tampilkan_mahasiswa()
kelas.tampilkan_mahasiswa_awal_DE()
