# FinTrack

FinTrack adalah aplikasi sederhana untuk mencatat pemasukan dan pengeluaran pribadi menggunakan Python.

Project ini saya buat untuk belajar membuat aplikasi dari dasar. Mulai dari input data, validasi, penyimpanan data, pengolahan transaksi, sampai penggunaan Git dan GitHub.

## Fitur

- Tambah pemasukan
- Tambah pengeluaran
- Melihat semua transaksi
- Melihat saldo
- Edit transaksi
- Hapus transaksi
- Laporan pengeluaran berdasarkan kategori
- Filter transaksi berdasarkan jenis
- Filter transaksi berdasarkan kategori
- Validasi nominal
- Validasi tanggal
- Validasi input agar tidak kosong
- ID transaksi otomatis
- Data disimpan menggunakan JSON

## Teknologi

- Python
- JSON
- Git
- GitHub

## Struktur Project

```text
fintrack/
│
├── main.py
├── transaction.py
├── storage.py
├── transactions.json
├── .gitignore
└── README.md
```

### Penjelasan File

**main.py**  
Berisi menu utama dan mengatur jalannya program.

**transaction.py**  
Berisi fungsi untuk mengelola transaksi seperti menambah, mengedit, menghapus, menampilkan, memfilter transaksi, menghitung saldo, dan membuat laporan pengeluaran.

**storage.py**  
Berisi fungsi untuk membaca dan menyimpan data transaksi ke file JSON.

**transactions.json**  
Digunakan untuk menyimpan data transaksi.

**.gitignore**  
Berisi file atau folder yang tidak perlu dimasukkan ke repository Git.

**README.md**  
Berisi informasi mengenai project dan cara menjalankan aplikasi.

## Cara Menjalankan

Pastikan Python sudah terinstall di komputer.

Clone repository dari GitHub:

```bash
git clone https://github.com/ZikriYahya/fintrack.git
```

Masuk ke folder project:

```bash
cd fintrack
```

Jalankan program:

```bash
python main.py
```

Setelah program dijalankan, menu utama akan muncul di terminal.

## Tampilan Menu

```text
================================
           FINTRACK
    Personal Finance Tracker
================================
1. Tambah pemasukan
2. Tambah pengeluaran
3. Lihat transaksi
4. Lihat saldo
5. Edit transaksi
6. Hapus transaksi
7. Laporan pengeluaran
8. Filter transaksi
9. Keluar

Pilih menu:
```

## Cara Kerja Singkat

Saat program dijalankan, FinTrack akan membaca data yang tersimpan di `transactions.json`.

Pengguna kemudian dapat memilih menu yang tersedia, misalnya menambahkan pemasukan atau pengeluaran.

Setiap transaksi memiliki beberapa data:

- ID transaksi
- Jenis transaksi
- Tanggal
- Nominal
- Kategori
- Keterangan

Contoh data transaksi:

```json
{
    "id": 1,
    "jenis": "pemasukan",
    "tanggal": "2026-11-11",
    "nominal": 100000,
    "kategori": "gaji",
    "keterangan": "contoh gaji"
}
```

Setiap kali ada perubahan data, seperti menambah, mengedit, atau menghapus transaksi, data akan disimpan kembali ke `transactions.json`.

## Contoh Penggunaan

Misalnya pengguna menambahkan pemasukan:

```text
===== TAMBAH PEMASUKAN =====
Tanggal (YYYY-MM-DD): 2026-09-21
Nominal: Rp500000
Kategori: gaji
Keterangan: uang bulanan

Pemasukan berhasil ditambahkan!
ID transaksi: 1
```

Kemudian pengguna menambahkan pengeluaran:

```text
===== TAMBAH PENGELUARAN =====
Tanggal (YYYY-MM-DD): 2026-09-21
Nominal: Rp20000
Kategori: makanan
Keterangan: makan siang

Pengeluaran berhasil ditambahkan!
ID transaksi: 2
```

Dari data tersebut, program dapat menghitung saldo secara otomatis:

```text
===== RINGKASAN KEUANGAN =====
Total pemasukan  : Rp500000
Total pengeluaran: Rp20000
Saldo            : Rp480000
```

## Validasi Input

FinTrack memiliki validasi sederhana untuk mengurangi kesalahan saat memasukkan data.

Nominal tidak boleh 0 atau bernilai negatif:

```text
Nominal: Rp-5000
Nominal harus lebih dari 0.
```

Program juga memeriksa format tanggal:

```text
Tanggal (YYYY-MM-DD): 21-09-2026
Format tanggal salah. Contoh: 2026-09-21
```

Input kategori dan keterangan juga tidak boleh kosong.

## Penyimpanan Data

Data FinTrack disimpan secara lokal menggunakan file `transactions.json`.

Dengan menggunakan JSON, data tetap tersedia walaupun program ditutup dan dijalankan kembali.

Contoh struktur data:

```json
[
    {
        "id": 1,
        "jenis": "pemasukan",
        "tanggal": "2026-09-21",
        "nominal": 500000,
        "kategori": "gaji",
        "keterangan": "uang bulanan"
    },
    {
        "id": 2,
        "jenis": "pengeluaran",
        "tanggal": "2026-09-21",
        "nominal": 20000,
        "kategori": "makanan",
        "keterangan": "makan siang"
    }
]
```

## Tujuan Project

Tujuan utama pembuatan FinTrack adalah untuk memahami dasar-dasar pengembangan aplikasi menggunakan Python.

Beberapa hal yang dipelajari dari project ini antara lain:

- Penggunaan variabel dan tipe data
- Conditional statement
- Perulangan
- Function
- List dan dictionary
- Input dan validasi data
- Pengolahan file JSON
- Pemisahan kode ke beberapa file
- CRUD sederhana
- Pengelolaan data berdasarkan ID
- Penggunaan Git
- Penggunaan GitHub
- Pengembangan project secara bertahap

## Pengembangan Selanjutnya

Project ini masih akan dikembangkan secara bertahap.

Rencana pengembangan selanjutnya antara lain:

- Menggunakan database SQLite
- Membuat tampilan menggunakan HTML dan CSS
- Menambahkan JavaScript
- Membuat backend menggunakan Python
- Menambahkan API
- Menambahkan sistem pencarian transaksi
- Menambahkan statistik keuangan
- Menambahkan grafik pemasukan dan pengeluaran
- Menambahkan testing
- Menambahkan GitHub Actions

## Status Project

**Status: Dalam Pengembangan**

FinTrack saat ini masih berupa aplikasi berbasis terminal (CLI) dengan Python dan penyimpanan data menggunakan JSON.

Fitur akan terus dikembangkan secara bertahap sambil mempelajari teknologi dan konsep baru.

## Repository

Source code project ini tersedia di GitHub:

https://github.com/ZikriYahya/fintrack