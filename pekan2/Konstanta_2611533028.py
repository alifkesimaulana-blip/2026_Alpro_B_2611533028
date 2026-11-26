# Buat file dengan nama Konstanta_2611533028.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_3028

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3028 = float(input('Masukkan nilai jari-jari: '))
luas_3028 = PI * jari_3028 * jari_3028
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3028, luas_3028))