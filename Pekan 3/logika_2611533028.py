# Buat file dengan nama logika_2611533028.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_3028
# Progaram ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai Boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_3028 =  input("Inout nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3028 =  input("Inout nilai boolean-1 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3028)
print("\nA2 =", a2_3028)

# Konjungsi: bernilai True jika keduanya True
hasil_3028 = a1_3028 and a2_3028
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3028)

# Disjungsi: bernilai True jika keduanya True
hasil_3028 = a1_3028 or a2_3028
print("\nDisjungsi (OR)")
print("A1 OR A2 =", hasil_3028)

# Negasi A1: membalik nilai A1
hasil_3028 = not a1_3028
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3028)

# Negasi A2: membalik nilai A2
hasil_3028 = not a2_3028
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3028)

# XOR: bernilai True jika kedua nilai berbeda
hasil_3028 = a1_3028 != a2_3028
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3028)

#