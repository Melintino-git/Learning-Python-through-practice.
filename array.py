#Melintino Siswoyo
#Membuat Array (list di python)
#angka = [10, 20, 30, 40, 50]

#Mengakses elemen
#print(angka[0]) #output: 10
#print(angka[1]) #output : 20
#print(angka[4]) #output : 50

#Mengubah elemen
#angka[1] = 25
#print(angka) #output : [10, 25, 30, 40, 50]

#Melintino Siswoyo
#Membuat Hashmap.

"""buah = {
    "apel" : "merah atau hijau",
    "pisang" : "kuning",
    "jeruk" : "orange"
}

#Mengakses value dengan key
print(buah["apel"]) #output : merah atau hijau
print(buah["pisang"]) #output : kuning
print(buah["jeruk"]) #output : orange

#Menambah pasangan key-value
buah["naga"] = "merah atau ungu"
print(buah)""" #dikomentar pake triple"

#Melintino Siswoyo
#Array sebagai stack

"""stack = []

#menambahkan elemen kedalam stack
def push(element) :
    stack.append(element)
    
#menghapus elemen terakhir (LIFO)
def pop():
    if len(stack) == 0:
        return "Stack kosong"
    else:
        return stack.pop()
    
#pemakaian
push(10)
push(20)
push(70)

print(pop()) #output : 70"""

#Melintino Siswoyo
#Array sebagai Queue

queue =[]

#Menambahkan elemen (enqueue)
def enqueue(element):
    queue.append(element)
    
#menghapus elemen pertama (dequeue)
def dequeue():
    if len(queue) == 0:
        return "queue kosong"
    else:
        return queue.pop(0)
    
#penggunaan
enqueue("pelanggan 1")
enqueue("pelanggan 2")
enqueue("pelanggan 3")

print(dequeue()) #output : pelanggan 1
print(queue) #output : ['pelanggan 2', 'pelanggan 3']
