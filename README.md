<img width="77" height="37" alt="image" src="https://github.com/user-attachments/assets/06382713-9efc-4483-b8c4-94fcd272fcf8" /># Mini Latihan Bertahap – Pemrograman Python

Repository ini berisi kumpulan latihan sederhana dalam bahasa Python yang dibuat untuk memenuhi tugas mata kuliah Pemrograman Dasar bersama Bapak Triyono, S.Kom di Program Studi Teknik Informatika – Universitas Duta Bangsa (UDB).

Seluruh tugas disusun secara bertahap (A sampai D) untuk memahami konsep kelas (class), atribut, enkapsulasi, relasi antar objek, dan pengolahan data sederhana.


## Struktur Proyek

```bash
Mini-Latihan-Bertahap/
├── A.py   → Pengenalan class Dosen
├── B.py   → Enkapsulasi dan validasi NIDN dengan property
├── C.py   → Relasi antar class (Ruang & KelasKuliah)
├── D.py   → Pengolahan data list & filtering objek Mahasiswa
```


## Penjelasan Setiap File

### A.py – Class Dasar (Pembuatan Objek)

Mengenalkan konsep dasar class dan instansiasi objek.
Program membuat dua objek Dosen dan menampilkan informasinya.

Fitur:

 - Konstruktor __init__ dengan atribut nidn dan nama.

 - Metode info() untuk menampilkan data dosen.

Contoh Output :

```bash
Dosen Triyono - 1234567890
Dosen Syailendra - 0987654321
```

### B.py – Enkapsulasi dan Property Setter

Latihan ini menambahkan validasi data menggunakan property pada class `Dosen`.

Fitur:

 - Menggunakan `_nidn` sebagai atribut privat.

 - Setter `@nidn.setter` untuk memastikan NIDN berisi angka dengan panjang tertentu.

 - Error handling ketika NIDN tidak sesuai format.

Contoh output (jika valid):

```bash
123456789
```

Contoh error (jika salah format):

```bash
ValueError: NIDN harus 9 digit angka.
```

### C.py – Relasi Antar Class

Latihan ini menunjukkan hubungan antar class (komposisi) antara `Ruang` dan `KelasKuliah`.

Fitur:

 - Class `Ruang` memiliki atribut `kode` dan `kapasitas`.

 - Class `KelasKuliah` berisi daftar `peserta` dan method untuk menambah mahasiswa.

 - Validasi agar jumlah peserta tidak melebihi kapasitas ruang.

Contoh output:

```bash
Tidak bisa menambahkan Irfan, kapasitas penuh!
Kelas TI-23A5 (3/3)
Peserta : - Gigieh
          - Luthfi
          - Lendraa
```

### D.py – Filter Data Objek

Latihan ini melatih pengolahan data berbasis list of objects.

Fitur:

 - Membuat daftar objek `Mahasiswa`.

 - Menampilkan hanya mahasiswa dengan huruf awal ‘D’ atau ‘E’.

Contoh output:

```bash
Mahasiswa dengan huruf awal D atau E:
- Dhiwa
- Desta
- Domingos
- Dosen
- Eka
```

## Cara Menjalankan Program

 1. Pastikan sudah menginstal Python 3.x

 2. Jalankan file yang diinginkan, misalnya:
    ```bash
    python A.py
    ```
 3. Lihat hasilnya di terminal.
