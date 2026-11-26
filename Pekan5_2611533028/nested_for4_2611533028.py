# Buat file dengan nama nested_for4_2611533028.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input ()

tinggi_3028 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3028 % 2 != 0:
    print("Tinggi pola harus bilangan genap")
else: 
    a_3028 = tinggi_3028
    c_3028 = a_3028
    lebar_3028 = (2 * tinggi_3028) - 2

    for i_3028 in range (1, tinggi_3028 + 1):
        b_3028 = c_3028 + 1

        for j_3028 in range (1, lebar_3028 + 1):

        # Baris atas dan bawah
         if i_3028 == 1 or i_3028 == tinggi_3028:
                print("#", end="")
         else:
                print(" = ", end="")

        # Baris isi
        else:
            if j_3028 == 1 or j_3028 == lebar_3028:
                 print(" | ", end="")
            elif j_3028 == c_3028:
                 print(" < ", end="")
            elif j_3028 == b_3028:
                 print(" > ", end="")
            elif j_3028 == (lebar_3028 - c_3028):
                 print(" < ", end="")
            elif j_3028 == (lebar_3028 - c_3028 + 1):
                 print(" > ", end="")
            elif j_3028 > b_3028 and j_3028 < ( lebar_3028 - c_3028):
                 print(" . ", end="")
            else:
                 print("   ", end="")
        print()

        # logika asli java
        a_3028 -= 2

        if a_3028 >= 0:
            c_3028 = ( -a_3028) + 2
        else:
            c_3028 = ( a_3028) 


