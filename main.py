import json
import os
from datetime import datetime

FILE_NAME = "transactions.json"


def load_transactions():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_transactions(transactions):
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)


def generate_id(transactions):
    if len(transactions) == 0:
        return 1

    ids = []

    for transaksi in transactions:
        ids.append(transaksi["id"])

    return max(ids) + 1


def input_nominal():
    while True:
        try:
            nominal = int(input("Nominal: Rp"))

            if nominal <= 0:
                print("Nominal harus lebih dari 0.")
                continue

            return nominal

        except ValueError:
            print("Nominal harus berupa angka.")


def input_date():
    while True:
        tanggal = input("Tanggal (YYYY-MM-DD): ")

        try:
            datetime.strptime(tanggal, "%Y-%m-%d")
            return tanggal

        except ValueError:
            print("Format tanggal salah. Contoh: 2026-09-21")


def show_transactions(transactions):
    print("\n===== DAFTAR TRANSAKSI =====")

    if len(transactions) == 0:
        print("Belum ada transaksi.")
        return

    for transaksi in transactions:
        print(f"\nID         : {transaksi['id']}")
        print(f"Jenis      : {transaksi['jenis'].upper()}")
        print(f"Tanggal    : {transaksi['tanggal']}")
        print(f"Nominal    : Rp{transaksi['nominal']}")
        print(f"Kategori   : {transaksi['kategori']}")
        print(f"Keterangan : {transaksi['keterangan']}")


def add_transaction(transactions, jenis):
    print(f"\n===== TAMBAH {jenis.upper()} =====")

    tanggal = input_date()
    nominal = input_nominal()

    kategori = input("Kategori: ")
    keterangan = input("Keterangan: ")

    transaksi = {
        "id": generate_id(transactions),
        "jenis": jenis,
        "tanggal": tanggal,
        "nominal": nominal,
        "kategori": kategori,
        "keterangan": keterangan
    }

    transactions.append(transaksi)
    save_transactions(transactions)

    print(f"\n{jenis.capitalize()} berhasil ditambahkan!")
    print(f"ID transaksi: {transaksi['id']}")


def delete_transaction(transactions):
    show_transactions(transactions)

    if len(transactions) == 0:
        return

    try:
        id_transaksi = int(
            input("\nMasukkan ID transaksi yang ingin dihapus: ")
        )

        transaksi_ditemukan = None

        for transaksi in transactions:
            if transaksi["id"] == id_transaksi:
                transaksi_ditemukan = transaksi
                break

        if transaksi_ditemukan is None:
            print("ID transaksi tidak ditemukan.")
            return

        transactions.remove(transaksi_ditemukan)

        save_transactions(transactions)

        print(
            f"Transaksi '{transaksi_ditemukan['keterangan']}' "
            "berhasil dihapus."
        )

    except ValueError:
        print("ID harus berupa angka.")


def show_balance(transactions):
    pemasukan = 0
    pengeluaran = 0

    for transaksi in transactions:

        if transaksi["jenis"] == "pemasukan":
            pemasukan += transaksi["nominal"]

        elif transaksi["jenis"] == "pengeluaran":
            pengeluaran += transaksi["nominal"]

    saldo = pemasukan - pengeluaran

    print("\n===== RINGKASAN KEUANGAN =====")
    print(f"Total pemasukan  : Rp{pemasukan}")
    print(f"Total pengeluaran: Rp{pengeluaran}")
    print(f"Saldo            : Rp{saldo}")


def expense_report(transactions):
    categories = {}

    for transaksi in transactions:

        if transaksi["jenis"] == "pengeluaran":

            kategori = transaksi["kategori"]
            nominal = transaksi["nominal"]

            if kategori in categories:
                categories[kategori] += nominal
            else:
                categories[kategori] = nominal

    print("\n===== PENGELUARAN BERDASARKAN KATEGORI =====")

    if len(categories) == 0:
        print("Belum ada pengeluaran.")
        return

    for kategori, total in categories.items():
        print(f"{kategori:<15} Rp{total}")


def filter_transactions(transactions):
    print("\n===== FILTER TRANSAKSI =====")
    print("1. Berdasarkan jenis")
    print("2. Berdasarkan kategori")
    print("3. Kembali")

    pilihan = input("\nPilih filter: ")

    if pilihan == "1":
        jenis = input(
            "Masukkan jenis (pemasukan/pengeluaran): "
        ).lower()

        hasil = []

        for transaksi in transactions:
            if transaksi["jenis"] == jenis:
                hasil.append(transaksi)

        if len(hasil) == 0:
            print("\nTidak ada transaksi dengan jenis tersebut.")
            return

        show_transactions(hasil)

    elif pilihan == "2":
        kategori = input("Masukkan kategori: ").lower()

        hasil = []

        for transaksi in transactions:
            if transaksi["kategori"].lower() == kategori:
                hasil.append(transaksi)

        if len(hasil) == 0:
            print("\nTidak ada transaksi dengan kategori tersebut.")
            return

        show_transactions(hasil)

    elif pilihan == "3":
        return

    else:
        print("\nPilihan tidak valid.")


transactions = load_transactions()


while True:

    print("\n================================")
    print("           FINTRACK")
    print("    Personal Finance Tracker")
    print("================================")

    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat transaksi")
    print("4. Lihat saldo")
    print("5. Hapus transaksi")
    print("6. Laporan pengeluaran")
    print("7. Filter transaksi")
    print("8. Keluar")

    pilihan = input("\nPilih menu: ")

    if pilihan == "1":
        add_transaction(transactions, "pemasukan")

    elif pilihan == "2":
        add_transaction(transactions, "pengeluaran")

    elif pilihan == "3":
        show_transactions(transactions)

    elif pilihan == "4":
        show_balance(transactions)

    elif pilihan == "5":
        delete_transaction(transactions)

    elif pilihan == "6":
        expense_report(transactions)

    elif pilihan == "7":
        filter_transactions(transactions)

    elif pilihan == "8":
        print("\nData tersimpan.")
        print("Terima kasih sudah menggunakan FinTrack!")
        break

    else:
        print("\nPilihan tidak valid.")