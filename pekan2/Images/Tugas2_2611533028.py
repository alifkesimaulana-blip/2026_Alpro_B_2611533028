 #Kode program tugas "Tugas2_2611533028.py"

from typing import Final

# Konstanta batas kelulusan
BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3028 = input("Masukkan Nama Mahasiswa\t\t: ")
jenis_kelamin_3028 = input("Masukkan Jenis Kelamin (L/P)\t: ")
umur_3028 = int(input("Masukkan Umur\t\t\t: "))
skor_tes_3028 = float(input("Masukkan Skor Tes Awal\t\t: "))

# Deklarasi alamat secara multiline
alamat_3028 = """Kebun Kopi, Kec. Jambi Selatan, Kota Jambi"""

# Token identifikasi menggunakan bilangan kompleks
token_3028 = 100+3j

# Evaluasi status kelulusan
status_lulus_3028 = skor_tes_3028 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa\t:", nama_3028, "| Tipe:", type(nama_3028))
print("Jenis Kelamin\t:", jenis_kelamin_3028, "| Tipe:", type(jenis_kelamin_3028))
print("Alamat Domisili\t:\n" + alamat_3028, "\n| Tipe:", type(alamat_3028))
print("Umur\t\t:", umur_3028, "tahun | Tipe:", type(umur_3028))
print("Skor Tes Awal\t:", skor_tes_3028, "| Tipe:", type(skor_tes_3028))
print("ID Token Sinyal\t:", token_3028, "| Tipe:", type(token_3028))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", status_lulus_3028, "| Tipe:", type(status_lulus_3028))