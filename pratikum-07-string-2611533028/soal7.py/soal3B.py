text = "Alif Maulana Kesi"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
   