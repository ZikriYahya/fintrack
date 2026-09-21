from storage import load_transactions
from transaction import (
    add_transaction,
    delete_transaction,
    expense_report,
    filter_transactions,
    show_balance,
    show_transactions
)


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