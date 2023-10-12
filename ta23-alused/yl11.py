# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

text = input("mingikiri: ")
mytext = text.strip()
center = int(len(mytext) / 2)

if len(mytext) >= 7 and len(mytext) % 2:
    print(mytext[center-1:center+2])

else:
    print("Error")

    