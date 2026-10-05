# KASIR OTOMATIS
# Program Kasir Otomatis Sederhana
# Melintino Siswoyo - UBP Karawang

keranjang = []

def tambah_item(nama, harga, jumlah):
    """Menambahkan item ke keranjang"""
    keranjang.append({
        "nama": nama,
        "harga": harga,
        "jumlah": jumlah
    })
    print(f"{jumlah} x {nama} ditambahkan ke keranjang.")

def tampilkan_keranjang():
    """Menampilkan isi keranjang"""
    print("\n=== Keranjang Belanja ===")
    if not keranjang:
        print("Keranjang kosong.")
    else:
        for item in keranjang:
            print(f"- {item['nama']} ({item['jumlah']} x Rp{item['harga']})")

def hitung_total():
    """Menghitung total belanja"""
    total = sum(item["harga"] * item["jumlah"] for item in keranjang)
    return total

def cetak_struk():
    """Mencetak struk belanja"""
    print("\n=== STRUK BELANJA ===")
    for item in keranjang:
        subtotal = item["harga"] * item["jumlah"]
        print(f"{item['nama']} - {item['jumlah']} x Rp{item['harga']} = Rp{subtotal}")
    print("----------------------------")
    print(f"TOTAL: Rp{hitung_total()}")
    print("Terima kasih telah berbelanja!")

def menu():
    """Menu utama kasir"""
    while True:
        print("\n=== MENU KASIR ===")
        print("1. Tambah Item")
        print("2. Tampilkan Keranjang")
        print("3. Cetak Struk & Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama barang: ")
            harga = int(input("Harga barang: "))
            jumlah = int(input("Jumlah: "))
            tambah_item(nama, harga, jumlah)
        elif pilihan == "2":
            tampilkan_keranjang()
        elif pilihan == "3":
            cetak_struk()
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    menu()
