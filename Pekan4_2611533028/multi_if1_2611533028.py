# Buat file dengan nama multi_if1_2611533028.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3028 = int(input("Input Umur Anda = "))
sim_3028 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_3028 >= 17 and sim_3028 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_3028 >= 17 and sim_3028 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_3028 < 17 and sim_3028 != "y":
    print("Anda Belum Cukup Umur punya SIM")

if umur_3028 < 17 and sim_3028 == "y":
    print("Anda Belum Cukup Umur bawa Motor")