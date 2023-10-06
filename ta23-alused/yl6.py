# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). (loogikatehted - logic operators)
# Küsi kasutajalt arv 1
# küsi kasutajalt arv 2
# küsi kasutajalt arv 3

nr1 = input("Sisesta 1. arv: ")
nr2 = input("Sisesta 2. arv: ")
nr3 = input("Sisesta 3. arv: ")

if int(nr1) > int(nr2) and int(nr1) > int(nr3):
  print("Maksimum arv on: ", nr1)
elif int(nr2) > int(nr3):
  print("maksimum arv on: ", nr2)
else:
  print("maksmimum arv on: ", nr3)
 