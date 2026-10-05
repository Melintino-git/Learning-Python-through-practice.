# Program Perpustakaan Otomatis
# Melintino Siswoyo - UBP Karawang

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status = "Tersedia"

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = [
            Buku("Pemrograman Python", "Guido van Rossum"),
            Buku("Teori Otomata", "Hopcroft & Ullman"),
            Buku("Struktur Data", "Narasimha Karumanchi")
        ]

    def tampilkan_stok(self):
        print("\n=== Daftar Stok Buku ===")
        for i, buku in enumerate(self.daftar_buku, start=1):
            print(f"{i}. {buku.judul} - {buku.penulis} [{buku.status}]")

    def pinjam_buku(self):
        self.tampilkan_stok()
        try:
            pilihan = int(input("\nMasukkan nomor buku yang ingin dipinjam: "))
            if 1 <= pilihan <= len(self.daftar_buku):
                self.daftar_buku[pilihan - 1].pinjam()
            else:
                print("Nomor buku tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

# Program utama
perpus = Perpustakaan()

while True:
    print("\n=== Menu Perpustakaan Otomatis ===")
    print("1. Daftar Stok Buku")
    print("2. Pinjaman Buku")
    print("3. Keluar")

    menu = input("Pilih menu (1/2/3): ")

    if menu == "1":
        perpus.tampilkan_stok()
    elif menu == "2":
        perpus.pinjam_buku()
    elif menu == "3":
        print("Terima kasih telah menggunakan sistem perpustakaan otomatis!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
