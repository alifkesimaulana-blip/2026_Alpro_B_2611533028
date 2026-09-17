# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n========================================")
print("3. OPERATOR BITWISE")
print("========================================")

angka1_3028 = int(input("Masukkan angka bitwise-1: "))
angka2_3028 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_3028 =", angka1_3028, "| biner =", bin(angka1_3028))
print("angka2_3028 =", angka2_3028, "| biner =", bin(angka2_3028))

# Bitwise AND
hasil_3028 = angka1_3028 & angka2_3028
print("\nBitwise AND (&)")
print(angka1_3028, "&", angka2_3028, "=", hasil_3028)
print("Biner hasil =", bin(hasil_3028))
print("Biner hasil (8 bit) =", format(hasil_3028, "08b"))

# Bitwise OR
hasil_3028 = angka1_3028 | angka2_3028
print("\nBitwise OR (|)")
print(angka1_3028, "|", angka2_3028, "=", hasil_3028)
print("Biner hasil =", bin(hasil_3028))
print("Biner hasil (8 bit) =", format(hasil_3028, "08b"))

# Bitwise XOR
hasil_3028 = angka1_3028 ^ angka2_3028
print("\nBitwise XOR (^)")
print(angka1_3028, "^", angka2_3028, "=", hasil_3028)
print("Biner hasil =", bin(hasil_3028))
print("Biner hasil (8 bit) =", format(hasil_3028, "08b"))

# Bitwise NOT
hasil_3028 = ~angka1_3028
print("\nBitwise NOT (~)")
print("~", angka1_3028, "=", hasil_3028)
print("Biner hasil =", bin(hasil_3028))
print("Biner hasil (8 bit) =", format(hasil_3028, "08b"))

# Bitwise geser kiri
jumlah_geser_3028 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3028 = angka1_3028 << jumlah_geser_3028
print("\nBitwise geser kiri (<<)")
print(angka1_3028, "<<", jumlah_geser_3028, "=", hasil_3028)
print("Biner hasil =", bin(hasil_3028))
print("Biner hasil (8 bit) =", format(hasil_3028, "08b"))

# Bitwise geser kanan
hasil_3028 = angka1_3028 >> jumlah_geser_3028
print("\nBitwise geser kanan (>>)")
print(angka1_3028, ">>", jumlah_geser_3028, "=", hasil_3028)
print("Biner hasil =", bin(hasil_3028))
print("Biner hasil (8 bit) =", format(hasil_3028, "08b"))