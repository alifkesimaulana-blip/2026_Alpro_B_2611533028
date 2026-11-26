# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_3028
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan  identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3028 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3028 = [int(angka.strip()) for angka in input_data_3028.split(",")]

nilai_dicari_3028 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3028 = nilai_dicari_3028 in data_3028
print("\nOperator keanggotaan IN")
print(nilai_dicari_3028, "in", data_3028, "=", hasil_3028)

# Operator not in
hasil_3028 = nilai_dicari_3028 not in data_3028
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3028, "not in", data_3028, "=", hasil_3028)

print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_3028 = data_3028

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3028 = objek1_3028

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3028 = data_3028.copy()

print("objek1 =", objek1_3028)
print("objek2 =", objek2_3028)
print("objek3 =", objek3_3028)

# Operator is
hasil_3028 = objek1_3028 is objek2_3028
print("\nOperator identitas IS")
print("objek1_3028 is objek2_3028 =", hasil_3028)

# Operator is not
hasil_3028 = objek1_3028 is not objek3_3028
print("\nOperator identitas IS NOT")
print("objek1_3028 is not objek3_3028 =", hasil_3028)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_3028 is objek3_3028 =", objek1_3028 is objek3_3028)
print("objek1_3028 == objek3_3028 =", objek1_3028 == objek3_3028)