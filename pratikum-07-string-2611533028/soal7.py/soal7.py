# Nama : Alif Maulana Kesi
# NIM : 2611533028
# Question 7
# Tampilkan kartu mahasiswa dengan datamu sendiri, persis dengan format contoh berikut.
# Lebar kartu 30 karakter, dan judul berada di tengah.
# Label rata kiri dengan lebar 10 karakter.
# Simpan nama dalam huruf kecil di variabel name, lalu tampilkan dengan title().
# Gunakan username dari Soal 6. Ambil angkatan dari NIM dengan slicing.

name = "alif maulana kesi"
nim = "2611533028"
username = "alif028"
angkatan = "20" + nim[:2]

print( "=" * 28)
print(" STUDENT CARD".center(28) )
print("=" * 28)
print("Nama:".ljust(10) + name.title() )
print("Username:".ljust(10) + username )
print("Angkatan:".ljust(10) + angkatan )
print("=" + "=" * 28 + "=")
