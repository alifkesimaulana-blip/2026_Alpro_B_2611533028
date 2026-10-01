# Buat file dengan nama jumlah_genap_2611533028.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input ()

ulang_3028 = int(input("Masukkan nilai batas: "))

jumlah_3028 = 0
for i_3028 in range(1, ulang_3028 + 1):
    if i_3028 % 2 == 0:
        print(i_3028, end=" ")
        jumlah_3028 = jumlah_3028 + i_3028

        if i_3028 < ulang_3028:
            print(" + ", end="")
        else:
            print("=", jumlah_3028, end="")
print()
print("jumlah =", jumlah_3028)