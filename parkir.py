# Program Parkir Otomatis Sederhana
# Melintino Siswoyo - UBP Karawang

import datetime

tarif_per_jam = 3000  # tarif parkir per jam
data_parkir = {}      # dictionary untuk menyimpan data kendaraan

def masuk_kendaraan(nopol):
    """Mencatat kendaraan masuk dengan waktu saat ini"""
    waktu_masuk = datetime.datetime.now()
    data_parkir[nopol] = waktu_masuk
    print(f"Kendaraan {nopol} masuk pada {waktu_masuk.strftime('%H:%M:%S')}")

def keluar_kendaraan(nopol):
    """Menghitung biaya parkir saat kendaraan keluar"""
    if nopol in data_parkir:
        waktu_masuk = data_parkir[nopol]
        waktu_keluar = datetime.datetime.now()
        lama = (waktu_keluar - waktu_masuk).seconds // 3600 + 1  # dibulatkan ke atas
        biaya = lama * tarif_per_jam
        print(f"Kendaraan {nopol} keluar pada {waktu_keluar.strftime('%H:%M:%S')}")
        print(f"Lama parkir: {lama} jam")
        print(f"Biaya parkir: Rp{biaya}")
        del data_parkir[nopol]  # hapus data setelah keluar
    else:
        print("Data kendaraan tidak ditemukan!")

def tampilkan_kendaraan():
    """Menampilkan daftar kendaraan yang sedang parkir"""
    print("\n=== Daftar Kendaraan Parkir ===")
    if not data_parkir:
        print("Tidak ada kendaraan di parkiran.")
    else:
        for nopol, waktu in data_parkir.items():
            print(f"{nopol} - masuk {waktu.strftime('%H:%M:%S')}")

def menu():
    """Menu utama parkir otomatis"""
    while True:
        print("\n=== MENU PARKIR ===")
        print("1. Kendaraan Masuk")
        print("2. Kendaraan Keluar")
        print("3. Tampilkan Kendaraan")
        print("4. Keluar Program")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nopol = input("Masukkan nomor polisi: ")
            masuk_kendaraan(nopol)
        elif pilihan == "2":
            nopol = input("Masukkan nomor polisi: ")
            keluar_kendaraan(nopol)
        elif pilihan == "3":
            tampilkan_kendaraan()
        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    menu()
