# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random
x = random.randint(0,101)

while True:
    y = int(input("Arva arv: "))
    if y < x:
        print("Suurem")
        continue
    elif y > x:
        print("väiksem")
        continue
    else:
        print("Õige")
        break





