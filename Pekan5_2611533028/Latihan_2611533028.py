tinggi_3028 = int(input("Masukkan tinggi segitiga : "))

for i_3028 in range(1, tinggi_3028 + 1):
  for j_3028 in range(tinggi_3028 - i_3028):
    print("", end= " ")
  for j_3028 in range( i_3028):
    print("*", end= " ")
  print()