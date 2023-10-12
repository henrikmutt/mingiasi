# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv.

# küsi tekst
# tekstist leia täishäälikud ("a", "e", "i", "o", "u", "õ", "ä", "ö", "ü")
# koosta nendest häälikutest list
# väljasta listi pikkus

text = input("sisesta tekst: ")
count = 0

vowels = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]

for i in range(len(text)):
    if text[i] in vowels:
        count += 1

print(count)







