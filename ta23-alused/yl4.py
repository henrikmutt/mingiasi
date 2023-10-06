# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). (muutuja - variable, tingimus - condition, if-lause - if statement)
# Küsi kasutajalt kaks numbrit
# Leia nende seast miinimum
# anna vastus

nr1 = input("sisesta 1. number: ")
nr2 = input("sisesta 2. number: ")
if int(nr1) < int(nr2):
    print("Miinimum arv on: ", nr1)
# if nr2 < nr1:
#     print("Miinimum arv on: ", nr2)
else:
    print("miinimum arv on: ",nr2)

# elif nr1 == nr2:
#     print("1. ja 2. arv on võrdsed")
