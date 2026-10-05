#ATM OTOMATIS

def atm_menu():
    saldo = 0
    while True:
        print("\n === MENU ATM ===")
        print("1. Setor tunai")
        print("2. Tarik tunai")
        print("3. Cek saldo")
        print("4. Keluar")
    
        pilihan = input("Pilih menu: ")
    
        if pilihan == "1":
            jumlah = int(input("Masukan jumlah setor: "))
            saldo+= jumlah
            print(f"Setoran berhasil. Saldo anda sekarang: Rp{saldo}")
        elif pilihan == "2":
            jumlah = int(input("Masukan jumlah penarikan: "))
            if jumlah <= saldo:
                saldo -= jumlah
                print(f"Penarikan berhasil. Saldo anda sekarang: Rp{saldo}")
            else: 
                print("Saldo tidak cukup!")
        elif pilihan == "3":
            print(f"Saldo anda : Rp{saldo}")
        elif pilihan == "4":
            print("Terimakasih telah menggunakan mesin ATM.")
            break
        else :
            print("Pilihan tidak valid, Silahkan coba lagi.")
        
atm_menu()




























def atm_menu():
    saldo = 0
    while True:
        print("\n=== MENU ATM===")
        print("1. Setor tunai")
        print("2. Tarik tunai")
        print("3. Cek saldo")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            jumlah = int(input("Masukan jumlah setor tunai : "))
            saldo += jumlah
            print(f"Setor tunai berhasil. Saldo sekarang : Rp.{saldo}")
        elif pilihan == "2":
            jumlah = int(input("Masukan jumlah penarikan : "))
            if jumlah <= saldo:
                saldo -= jumlah
                print(f"Penarikan tunai berhasil. Saldo sekarang : Rp.{saldo}")
        elif pilihan == "3":
            print(f"Saldo saat ini : Rp.{saldo}")
        elif pilihan == "4":
            print("Terimakasih telah menggunakan ATM.")
            break
        else:
            print("Pilihan tidak Valid! Silahkan mencoba kembali.")
atm_menu()