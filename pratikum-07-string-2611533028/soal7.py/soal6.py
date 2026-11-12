# Nama : Alif Maulana Kesi
# NIM : 2611533028
# Question 6

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

full_name = "  Alif Maulana Kesi  "
nim = "2611533028"
clean = full_name.strip()
space = clean.find(" ")
if space != -1:
    first_name = clean[:space].lower()
    username = first_name + nim[-3:]
else:
    username = clean.lower() + nim[-3:]

print("Username:", username)