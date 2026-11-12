# Name: Alif Maulana Kessi
# NIM: 2611533028
# Question 5 (B)

nim = input("NIM: ")
if len(nim) == 10 and nim.isdigit():
    print("Valid, intake year 20" + nim[:2])
else:
    print("Invalid NIM")