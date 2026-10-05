#latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan for

#dummy variable

print("Awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
    
print("Akhir dari for") 
   
# 2. Menggunakan while

print("Awal While")
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break
    
print("Akhir While")

# 3. Hanya ganjil saja

print("Awal While")
count = 1
while True:
    if (count%2):
    #print jika ganjil
        print("*"*count)
        count += 1
    else:
    # akan kembali ke atas jika ganjil
        count += 1
        continue
    # akan break ketika melebihi sisi
    if count > sisi:
        break
    
print("Akhir While")


# 4. Belah ketupat

print("awal tugas")
count = 1
spasi = int(sisi/2)
#sisi atas
while True:
    if (count%2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
#sisi bawah
count = sisi + 1
while True:
    if(count%2):
        spasi += 1
        print(" "*spasi, "+"*count)
        count -= 1
    else:
        count -= 1
        continue
    if count < 1:
        break
    
print("akhir tugas")