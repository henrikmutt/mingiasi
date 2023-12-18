# 2*l*w + 2*w*h + 2*h*l
# Muuda string listiks
# leia listist kõige väiksem väärtus, liida kogu tehtele see väärtus
# Tee nende elementidega see tehe

fulltotal = 0

with open ('file.txt') as f:
    for item in f:
        list = item.strip()
        stringlist = list.split("x")
        list = [eval(i) for i in stringlist]
        sideA = list[0] * list[1]
        sideB = list[1] * list[2]
        sideC = list[2] * list[0]
        sidelist = [sideA, sideB, sideC]
        sidelist.sort()
        area = 2 * sideA + 2 * sideB + 2 * sideC
        total = area + sidelist[0]
        fulltotal += total
        print(fulltotal)
        



# loop, mis teeb iga reaga selle tehte
# tee muutuja "fulltotal" väärtusega 0.
# iga rea tulemus liidetakse fulltotalile (loop)
# väljastatakse lõppsumma

