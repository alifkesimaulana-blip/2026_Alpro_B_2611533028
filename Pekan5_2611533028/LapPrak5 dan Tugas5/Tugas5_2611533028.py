# tugas5_2611533028.py
# Pola Jam Pasir Kristal Palindromik Berbingkai (Pekan 5)
# Program dijalankan 2 kali berturut-turut (Uji Coba 1 dan Uji Coba 2)
# Menggunakan perulangan for bersarang murni (tanpa perkalian string)

for uji_3028 in range(2):
    print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
    n_3028 = int(input("Masukkan ukuran skala jam pasir (N): "))

    # ---------- Bingkai atas ----------
    print("#", end="")
    for garis_3028 in range(4 * n_3028 + 5):
        print("=", end="")
    print("#", end="")
    print()

    # ---------- Fase 1: jam pasir atas (baris N turun s.d. 1) ----------
    for baris_3028 in range(n_3028, 0, -1):
        print("| ", end="")
        for spasi_3028 in range(2 * (n_3028 - baris_3028)):
            print(" ", end="")
        for angka_3028 in range(baris_3028, 0, -1):
            print(angka_3028, end=" ")
        print("<*>", end="")
        for angka_3028 in range(1, baris_3028 + 1):
            print(" ", end="")
            print(angka_3028, end="")
        for spasi_3028 in range(2 * (n_3028 - baris_3028)):
            print(" ", end="")
        print(" |", end="")
        print()

    # ---------- Fase 2: poros titik pusat ----------
    print("|", end="")
    for spasi_3028 in range(2 * n_3028 + 1):
        print(" ", end="")
    print("<*>", end="")
    for spasi_3028 in range(2 * n_3028 + 1):
        print(" ", end="")
    print("|", end="")
    print()

    # ---------- Fase 3: jam pasir bawah (baris 1 naik s.d. N) ----------
    for baris_3028 in range(1, n_3028 + 1):
        print("| ", end="")
        for spasi_3028 in range(2 * (n_3028 - baris_3028)):
            print(" ", end="")
        for angka_3028 in range(baris_3028, 0, -1):
            print(angka_3028, end=" ")
        print("<*>", end="")
        for angka_3028 in range(1, baris_3028 + 1):
            print(" ", end="")
            print(angka_3028, end="")
        for spasi_3028 in range(2 * (n_3028 - baris_3028)):
            print(" ", end="")
        print(" |", end="")
        print()

    # ---------- Bingkai bawah ----------
    print("#", end="")
    for garis_3028 in range(4 * n_3028 + 5):
        print("=", end="")
    print("#", end="")
    print()
