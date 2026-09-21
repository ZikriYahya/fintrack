from datetime import datetime

from storage import save_transactions


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


def input_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("Input tidak boleh kosong.")
            continue

        return text


def input_date():
    while True:
        tanggal = input("Tanggal (YYYY-MM-DD): ")

        try:
            datetime.strptime(tanggal, "%Y-%m-%d")
            return tanggal

        except ValueError:
            print("Format tanggal salah. Contoh: 2026-09-21")


def validate_transaction_type(jenis):
    jenis_valid = ["pemasukan", "pengeluaran"]

    if jenis not in jenis_valid:
        print("Jenis transaksi tidak valid.")
        return False

    return True


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

    if not validate_transaction_type(jenis):
        return

    print(f"\n===== TAMBAH {jenis.upper()} =====")

    tanggal = input_date()
    nominal = input_nominal()

    kategori = input_text("Kategori: ")
    keterangan = input_text("Keterangan: ")

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


def edit_transaction(transactions):
    show_transactions(transactions)

    if len(transactions) == 0:
        return

    try:
        id_transaksi = int(
            input("\nMasukkan ID transaksi yang ingin diedit: ")
        )

        transaksi_ditemukan = None

        for transaksi in transactions:
            if transaksi["id"] == id_transaksi:
                transaksi_ditemukan = transaksi
                break

        if transaksi_ditemukan is None:
            print("ID transaksi tidak ditemukan.")
            return

        print("\n===== EDIT TRANSAKSI =====")
        print("Kosongkan input jika ingin mempertahankan data lama.")

        tanggal = input(
            f"Tanggal [{transaksi_ditemukan['tanggal']}]: "
        ).strip()

        if tanggal != "":
            try:
                datetime.strptime(tanggal, "%Y-%m-%d")
                transaksi_ditemukan["tanggal"] = tanggal

            except ValueError:
                print("Format tanggal salah.")
                return

        nominal = input(
            f"Nominal [Rp{transaksi_ditemukan['nominal']}]: "
        ).strip()

        if nominal != "":
            try:
                nominal = int(nominal)

                if nominal <= 0:
                    print("Nominal harus lebih dari 0.")
                    return

                transaksi_ditemukan["nominal"] = nominal

            except ValueError:
                print("Nominal harus berupa angka.")
                return

        kategori = input(
            f"Kategori [{transaksi_ditemukan['kategori']}]: "
        ).strip()

        if kategori != "":
            transaksi_ditemukan["kategori"] = kategori

        keterangan = input(
            f"Keterangan [{transaksi_ditemukan['keterangan']}]: "
        ).strip()

        if keterangan != "":
            transaksi_ditemukan["keterangan"] = keterangan

        save_transactions(transactions)

        print("\nTransaksi berhasil diperbarui.")

    except ValueError:
        print("ID harus berupa angka.")


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