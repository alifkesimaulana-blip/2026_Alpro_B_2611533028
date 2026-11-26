print("=== SISTEM RESERVASI TIKET BIOSKOP ===")

# ------------------------------
# 1. Input data penonton
# ------------------------------
nama_3028 = input("Masukkan Nama Penonton : ")
status_member_3028 = input("Masukkan Status Keanggotaan (member/nonmember) : ")
total_harga_3028 = int(input("Masukkan Total Harga Tiket : "))
jumlah_tiket_3028 = int(input("Masukkan Jumlah Tiket : "))
kode_voucher_3028 = input("Masukkan Kode Voucher : ")

# ------------------------------
# 2. Menampilkan data reservasi
# ------------------------------
print("\n=== DATA RESERVASI ===")
print(f"Nama Penonton           : {nama_3028}")
print(f"Status Keanggotaan      : {status_member_3028}")
print(f"Total Harga Tiket       : Rp{total_harga_3028}")
print(f"Jumlah Tiket            : {jumlah_tiket_3028}")
print(f"Kode Voucher            : {kode_voucher_3028}")

# ------------------------------
# 3. Validasi syarat-syarat
# ------------------------------
daftar_voucher_3028 = ["NONTON10", "NONTON20", "HEMATWEEKEND", "SPESIALMHS"]  # daftar voucher valid

syarat_harga_3028 = total_harga_3028 >= 150000            # syarat minimal transaksi
syarat_jumlah_3028 = jumlah_tiket_3028 >= 2               # syarat minimal jumlah tiket
status_valid_3028 = status_member_3028 == "member"        # cek status member
voucher_valid_3028 = kode_voucher_3028 in daftar_voucher_3028  # cek voucher ada di daftar

print("\n=== HASIL VALIDASI ===")
print(f"Harga >= Rp150000       : {syarat_harga_3028}")
print(f"Jumlah Tiket >= 2       : {syarat_jumlah_3028}")
print(f"Status Member           : {status_valid_3028}")
print(f"Voucher Tersedia        : {voucher_valid_3028}")
print(f"Mendapatkan Diskon      : {syarat_harga_3028 or syarat_jumlah_3028}")
print(f"Mendapatkan Voucher     : {voucher_valid_3028}")

# ------------------------------
# 4. Perhitungan pembayaran
# ------------------------------
diskon = 0.10

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                  : Rp{diskon * total_harga_3028}")
print(f"Total Pembayaran        : Rp{total_harga_3028 - total_harga_3028 * diskon}")
print(f"Rata-rata Harga Tiket   : Rp{total_harga_3028 / jumlah_tiket_3028}")

# ==========================================
# 5. HAK AKSES PENONTON (encoding ke bit)
# ==========================================
print("\n=== HAK AKSES PENONTON ===")
print("Kode Hak Akses          : bit0=Member, bit1=Harga, bit2=Jumlah, bit3=Voucher")
print(f"Member Access           : {status_valid_3028}")
print(f"Voucher Access          : {voucher_valid_3028}")
print("Studio Premium Access   : ...")

# Menggabungkan 4 status boolean menjadi satu kode biner 4-bit
kode_reservasi_3028 = int(status_valid_3028) << 0 | int(syarat_harga_3028) << 1 | int(syarat_jumlah_3028) << 2 | int(voucher_valid_3028) << 3
kode_referensi_3028 = int(status_valid_3028) << 0 | int(syarat_harga_3028) << 1 | int(voucher_valid_3028) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Reservasi ===")
print(f"{format(int(status_valid_3028) << 0, '04b')} | {format(int(syarat_harga_3028) << 1, '04b')} | "
      f"{format(int(syarat_jumlah_3028) << 2, '04b')} | {format(int(voucher_valid_3028) << 3, '04b')}")
print(f"Kode Biner              : {format(kode_reservasi_3028, '04b')}")
print(f"Kode Desimal            : {kode_reservasi_3028}")

print("\n=== Pemeriksaan Status (AND) ===")
print("Cek Member")
print(f"{format(kode_reservasi_3028, '04b')} & {format(int(status_valid_3028) << 0, '04b')}")
print(f"Hasil Biner    : {format(kode_reservasi_3028 & (int(status_valid_3028) << 0), '04b')}")
print(f"Hasil Desimal  : {kode_reservasi_3028 & (int(status_valid_3028) << 0)}")

print("Cek Voucher")
print(f"{format(kode_reservasi_3028, '04b')} & {format(int(voucher_valid_3028) << 3, '04b')}")
print(f"Hasil Biner    : {format(kode_reservasi_3028 & (int(voucher_valid_3028) << 3), '04b')}")
print(f"Hasil Desimal  : {kode_reservasi_3028 & (int(voucher_valid_3028) << 3)}")

print("\n=== Perbandingan Status (XOR) ===")
print(f"Kode Reservasi : {format(kode_reservasi_3028, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_3028, '04b')}")
print(f"{format(kode_reservasi_3028, '04b')} ^ {format(kode_referensi_3028, '04b')}")
print(f"Hasil Biner    : {format(kode_reservasi_3028 ^ kode_referensi_3028, '04b')}")
print(f"Hasil Desimal  : {kode_reservasi_3028 ^ kode_referensi_3028}")

print("\n=== Shift (Upgrade Level Akses) ===")
print(f"{format(kode_reservasi_3028, '04b')} << 1")
print(f"Hasil Biner    : {format(kode_reservasi_3028 << 1, '04b')}")
print(f"Hasil Desimal  : {kode_reservasi_3028 << 1}")

print("\n=== SELESAI ===")
