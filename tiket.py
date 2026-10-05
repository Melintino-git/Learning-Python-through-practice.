# Program Tiket Otomatis Sederhana
# Melintino Siswoyo - UBP Karawang

tiket_list = [
    {"nama": "Konser Musik", "harga": 100000},
    {"nama": "Bioskop", "harga": 50000},
    {"nama": "Kereta Ekonomi", "harga": 75000},
    {"nama": "Kereta Eksekutif", "harga": 150000}
]

def tampilkan_tiket():
    """Menampilkan daftar tiket yang tersedia"""
    print("\n=== Daftar Tiket ===")
    for i, t in enumerate(tiket_list, start=1):
        print(f"{i}. {t['nama']} - Rp{t['harga']}")

def beli_tiket(pilihan, jumlah):
    """Menghitung total harga tiket"""
    if 1 <= pilihan <= len(tiket_list):
        tiket = tiket_list[pilihan - 1]
        total = tiket["harga"] * jumlah
        print(f"\nAnda membeli {jumlah} tiket {tiket['nama']}.")
        print(f"Total harga: Rp{total}")
    else:
        print("Pilihan tiket tidak valid!")

def menu():
    """Menu utama program tiket"""
    while True:
        print("\n=== MENU TIKET ===")
        print("1. Lihat Daftar Tiket")
        print("2. Beli Tiket")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_tiket()
        elif pilihan == "2":
            tampilkan_tiket()
            pilih = int(input("Pilih nomor tiket: "))
            jumlah = int(input("Masukkan jumlah tiket: "))
            beli_tiket(pilih, jumlah)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem tiket.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    menu()
