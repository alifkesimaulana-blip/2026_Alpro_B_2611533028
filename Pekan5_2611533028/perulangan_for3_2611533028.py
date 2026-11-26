# Buat lah file dengan nama perulangan_for3_2611533028.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input ()

ulang_3028 = int(input("Masukkan jumlah perulangan: "))

jumlah_3028 = 0
for i in range(1, ulang_3028 + 1):
    print(i, end=" ")
    jumlah_3028 = jumlah_3028+ i

    if i < ulang_3028:
        print(" + ", end="")
    else:
        print("=", jumlah_3028, end="")
print()
print("jumlah =", jumlah_3028)