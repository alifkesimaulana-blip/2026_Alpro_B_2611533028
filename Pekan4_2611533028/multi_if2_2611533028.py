# Buat file dengan nama multi_if2_2611533028.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_3028 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y atau 'ya')
input_member_3028 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_3028 = input_member_3028 in ["y", "ya"]

# Input satus kode promo (mengecek apakah user mengetik 'y atau 'ya')
input_promo_3028 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3028 = input_promo_3028 in ["y", "ya"]

total_diskon_persen_3028 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3028 > 1000000:
    total_diskon_persen_3028 += 10  # Diskon belanja besar 

if is_member_3028:
    total_diskon_persen_3028 += 5  # Diskon member

if kode_promo_valid_3028:
    total_diskon_persen_3028 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3028 = total_belanja_3028 * (total_diskon_persen_3028 / 100)
total_bayar_3028 = total_belanja_3028 - nominal_diskon_3028

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_3028}% (Rp {nominal_diskon_3028:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_3028:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_3028}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid