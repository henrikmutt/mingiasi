# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.

pet = input("Sisesta lemmikloom: ")
print(pet[0])

petlist = ["hobune", "naarits", "rebane"]
petlist.append(pet)
print(petlist)
print(petlist[-1][-1])