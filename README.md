# Mini Latihan Bertahap – Pemrograman Python

Repository ini berisi kumpulan latihan sederhana dalam bahasa Python yang dibuat untuk memenuhi tugas mata kuliah Pemrograman Python yang diberikan oleh Bapak Triyono, S.Kom | Program Studi Teknik Informatika – Universitas Duta Bangsa (UDB).

Dibuat menggunakan Python dengan pendekatan OOP (Object-Oriented Programming).


## Deskripsi Program

1. `Dosen`
2. `Ruang`
3. `Kelas Kuliah`

## Alur Program

1. Membuat objek dosen:
   
   ```bash
   dosen1 = Dosen("1234567890", "Triyono")
   dosen2 = Dosen("09876543212345", "Syailendra")  # Akan error karena NIDN lebih dari 10 digit
   ```

  Jika NIDN tidak valid, program akan menampilkan pesan kesalahan:

  ```bash
  NIDN harus terdiri dari 10 digit angka.
  ```

2. Membuat objek ruang:

   ```bash
   ruangA = Ruang("R101", 29)
   ```
   
4. Membuat objek kelas kuliah:

   ```bash
   kelas = KelasKuliah("TI - 23A5", ruangA)
   ```
   
6. Menambahkan daftar mahasiswa:

   ```bash
   for nama in daftar_mahasiswa:
   kelas.tambah_mahasiswa(nama)
   ```
   
8. Menampilkan hasil:

 - Seluruh mahasiswa di kelas

 - Mahasiswa dengan nama diawali huruf D atau E

## Contoh Output

```bash
NIDN harus terdiri dari 10 digit angka.
Dosen Triyono - 1234567890

Daftar Mahasiswa di TI - 23A5:
- Hafan
- Eka
- Aziz
- Irfan
- Minan
- Savina
- Trafika
- Lendra
- Luthfi
- Fitra
- Dhiwa
- Kahfi
- Desta
- Viqi
- Arsa
- Domingos
- Pratama
- Gigieh
- Faris
- Ridho
- Adit
- Bima
- Fahryan
- Nabil
- Najib
- Nathan
- Raihan
- Raka
- Rofi

Mahasiswa dengan nama diawali huruf D atau E:
- Eka
- Dhiwa
- Desta
- Domingos
```

## Konsep yang Digunakan

 - Object-Oriented Programming (OOP)

 - Validasi Input

 - Exception Handling (try-except)

 -  List dan Perulangan

 - Pencarian berdasarkan kondisi huruf awal

