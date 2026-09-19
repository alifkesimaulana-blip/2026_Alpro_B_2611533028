print("=== SISTEM RESERVASI TIKET BIOSKOP ===")

# ------------------------------
# 1. Input data penonton
# ------------------------------
nama = input("Masukkan Nama Penonton : ")
status_member = input("Masukkan Status Keanggotaan (member/nonmember) : ")
total_harga = int(input("Masukkan Total Harga Tiket : "))
jumlah_tiket = int(input("Masukkan Jumlah Tiket : "))
kode_voucher = input("Masukkan Kode Voucher : ")

# ------------------------------
# 2. Menampilkan data reservasi
# ------------------------------
print("\n=== DATA RESERVASI ===")
print(f"Nama Penonton           : {nama}")
print(f"Status Keanggotaan      : {status_member}")
print(f"Total Harga Tiket       : Rp{total_harga}")
print(f"Jumlah Tiket            : {jumlah_tiket}")
print(f"Kode Voucher            : {kode_voucher}")

# ------------------------------
# 3. Validasi syarat-syarat
# ------------------------------
daftar_voucher = ["NONTON10", "NONTON20", "HEMATWEEKEND", "SPESIALMHS"]  # daftar voucher valid

syarat_harga = total_harga >= 150000            # syarat minimal transaksi
syarat_jumlah = jumlah_tiket >= 2               # syarat minimal jumlah tiket
status_valid = status_member == "member"        # cek status member
voucher_valid = kode_voucher in daftar_voucher  # cek voucher ada di daftar

print("\n=== HASIL VALIDASI ===")
print(f"Harga >= Rp150000       : {syarat_harga}")
print(f"Jumlah Tiket >= 2       : {syarat_jumlah}")
print(f"Status Member           : {status_valid}")
print(f"Voucher Tersedia        : {voucher_valid}")
print(f"Mendapatkan Diskon      : {syarat_harga or syarat_jumlah}")
print(f"Mendapatkan Voucher     : {voucher_valid}")

# ------------------------------
# 4. Perhitungan pembayaran
# ------------------------------
diskon = 0.10

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                  : Rp{diskon * total_harga}")
print(f"Total Pembayaran        : Rp{total_harga - total_harga * diskon}")
print(f"Rata-rata Harga Tiket   : Rp{total_harga / jumlah_tiket}")

# ==========================================
# 5. HAK AKSES PENONTON (encoding ke bit)
# ==========================================
print("\n=== HAK AKSES PENONTON ===")
print("Kode Hak Akses          : bit0=Member, bit1=Harga, bit2=Jumlah, bit3=Voucher")
print(f"Member Access           : {status_valid}")
print(f"Voucher Access          : {voucher_valid}")
print("Studio Premium Access   : ...")

# Menggabungkan 4 status boolean menjadi satu kode biner 4-bit
kode_reservasi = int(status_valid) << 0 | int(syarat_harga) << 1 | int(syarat_jumlah) << 2 | int(voucher_valid) << 3
kode_referensi = int(status_valid) << 0 | int(syarat_harga) << 1 | int(voucher_valid) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Reservasi ===")
print(f"{format(int(status_valid) << 0, '04b')} | {format(int(syarat_harga) << 1, '04b')} | "
      f"{format(int(syarat_jumlah) << 2, '04b')} | {format(int(voucher_valid) << 3, '04b')}")
print(f"Kode Biner              : {format(kode_reservasi, '04b')}")
print(f"Kode Desimal            : {kode_reservasi}")

print("\n=== Pemeriksaan Status (AND) ===")
print("Cek Member")
print(f"{format(kode_reservasi, '04b')} & {format(int(status_valid) << 0, '04b')}")
print(f"Hasil Biner    : {format(kode_reservasi & (int(status_valid) << 0), '04b')}")
print(f"Hasil Desimal  : {kode_reservasi & (int(status_valid) << 0)}")

print("Cek Voucher")
print(f"{format(kode_reservasi, '04b')} & {format(int(voucher_valid) << 3, '04b')}")
print(f"Hasil Biner    : {format(kode_reservasi & (int(voucher_valid) << 3), '04b')}")
print(f"Hasil Desimal  : {kode_reservasi & (int(voucher_valid) << 3)}")

print("\n=== Perbandingan Status (XOR) ===")
print(f"Kode Reservasi : {format(kode_reservasi, '04b')}")
print(f"Kode Referensi : {format(kode_referensi, '04b')}")
print(f"{format(kode_reservasi, '04b')} ^ {format(kode_referensi, '04b')}")
print(f"Hasil Biner    : {format(kode_reservasi ^ kode_referensi, '04b')}")
print(f"Hasil Desimal  : {kode_reservasi ^ kode_referensi}")

print("\n=== Shift (Upgrade Level Akses) ===")
print(f"{format(kode_reservasi, '04b')} << 1")
print(f"Hasil Biner    : {format(kode_reservasi << 1, '04b')}")
print(f"Hasil Desimal  : {kode_reservasi << 1}")

print("\n=== SELESAI ===")
