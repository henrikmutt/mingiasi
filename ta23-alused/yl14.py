# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” (ext - extension - faili laiend) 
# ja prindib välja laiendi (“ext”). (str.split)

fail = (input("sisesta failinimi koos laiendiga: "))
x = fail.split(".")
print(x[-1])



