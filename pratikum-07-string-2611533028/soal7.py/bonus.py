# Nama : Alif Maulana Kesi
# NIM : 2611533028  
# Question Bonus

kalimat = input("Masukkan kalimat: ")

# Mengabaikan spasi dan huruf kapital
teks = kalimat.replace(" ", "").lower()

if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")