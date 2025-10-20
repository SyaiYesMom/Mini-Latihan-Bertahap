class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

mahasiswa_list = [
    Mahasiswa("Hafan"),
    Mahasiswa("Eka"),
    Mahasiswa("Aziz"),
    Mahasiswa("Irfan"),
    Mahasiswa("Minan"),
    Mahasiswa("Savina"),
    Mahasiswa("Trafika"),
    Mahasiswa("Lendra"),
    Mahasiswa("Luthfi"),
    Mahasiswa("Fitra"),
    Mahasiswa("Dhiwa"),
    Mahasiswa("Kahfi"),
    Mahasiswa("Desta"),
    Mahasiswa("Viqi"),
    Mahasiswa("Arsa"),
    Mahasiswa("Domingos"),
    Mahasiswa("Pratama"),
    Mahasiswa("Gigieh"),
    Mahasiswa("Faris"),
    Mahasiswa("Ridho"),
    Mahasiswa("Adit"),
    Mahasiswa("Bima"),
    Mahasiswa("Fahryan"),
    Mahasiswa("Nabil"),
    Mahasiswa("Najib"),
    Mahasiswa("Nathan"),
    Mahasiswa("Raihan"),
    Mahasiswa("Raka"),
    Mahasiswa("Rofi"),
]

print("Mahasiswa dengan huruf awal D atau E:")
for m in mahasiswa_list:
    if m.nama[0].upper() in ["D", "E"]:
        print("-", m.nama)
