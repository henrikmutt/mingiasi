# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

# Küsi kasutajalt positiivne täisarv
# tee selgeks, kas antud täisarv jagub neljasajaga või neljaga

year = int(input("Sisesta positiivne täisarv: "))

if year % 100 == 0 and year % 4 == 0 and year % 400 == 0:
    print("arv", year, "on liigaasta")

elif year % 100 == 0 and year % 4 == 0:
    print("arv", year, "on lihtaasta")

else:
    print("arv", year, "on liigaasta")



