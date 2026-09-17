# Buat file dengan nama assignment_2611533028
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_3028
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3028 = int(input("Input angka-1: "))
angka2_3028 = int(input("Input angka-2: "))

print("\nNilai awal angka1_3028 =", angka1_3028 )
print("Nilai angka2_3028 =", angka2_3028 )

# Assignment biasa
hasil_3028 = angka1_3028
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3028)

# Assignment penambahan 
hasil_3028 = angka1_3028
hasil_3028 += angka2_3028
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3028)

# Assignment pengurangan
hasil_3028 = angka1_3028
hasil_3028 -= angka2_3028
print("\nAssignment penambahan (-=)")
print("Hasil =", hasil_3028)

# Assignment perkalian
hasil_3028 = angka1_3028
hasil_3028 *= angka2_3028
print("\nAssignment penambahan (*=)")
print("Hasil =", hasil_3028)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3028 != 0:
    hasil_3028 = angka1_3028
    hasil_3028 /= angka2_3028
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3028)
    # Operator tambahan
    hasil_3028 = angka1_3028
    hasil_3028 //= angka2_3028
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3028)
    hasil_3028 = angka1_3028
    hasil_3028 %= angka2_3028
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3028)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0. ")

# Operator tambahan: assignment perpangkatan
hasil_3028 = angka1_3028
hasil_3028 **= angka2_3028
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3028)
