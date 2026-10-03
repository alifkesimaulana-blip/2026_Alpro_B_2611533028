# Buat file dengan nama if_elif_else1_2611533028.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3028 = int(input("Input Umur Anda = "))
sim_3028 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0]

if umur_3028 >= 17 and sim_3028 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_3028 >= 17 and sim_3028 != "y":
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3028 < 17 and sim_3028 == "y":
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")