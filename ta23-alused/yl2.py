# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)
# 1) küsi raadius
# 2) arvuta ringi pindala
# 3) arvuta ümbermõõt
# 4) väljasta vastused

import math
r = float (input("Sisesta raadius: "))
pi = math.pi
x = r * r * pi
y = 2 * pi * r
print("pindala:", round(x))
print("ümbermõõt", round(y))

