# Buat file dengan  nama aritmatika_2611533028.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terkahir contoh: angka1_3028 
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan di konversi menjadi tipe data integer 

angka1_3028 = int(input("input angka-1"))
angka2_3028 = int(input("input angka-2"))

# Penjumlahan
hasil_3028= angka1_3028 + angka2_3028
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3028)

# Pengurangan
hasil_3028= angka1_3028 - angka2_3028
print("\nOperator Pengurangan")
print("Hasil =", hasil_3028)

# Perkalian
hasil_3028= angka1_3028 * angka2_3028
print("\nOperator Perkalian")
print("Hasil =", hasil_3028)

# Pemabagian, pembagian bulat, dan sisa bagi
if angka2_3028 != 0:
    hasil_3028= angka1_3028 / angka2_3028
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3028)

    hasil_3028= angka1_3028 % angka2_3028
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3028)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil_3028= angka1_3028 ** angka2_3028
print("\nOperator Pangkat")
print("Hasil =", hasil_3028)
