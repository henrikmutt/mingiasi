# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)
# küsi kasutajalt täisarv
# tuvasta, kas on paarisarv või mitte
# anna vastus

nr = int(input("Sisesta täisarv: "))

if nr % 2:
    print("Arv", nr, "on paarituarv")
else:
    print("arv", nr, "on")

