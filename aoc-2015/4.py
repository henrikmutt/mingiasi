# liida 1. lühike külg iseendaga ja liida sellele 2. lühem külg + 2. lühem külg (Näide: 2x3x4 -> 2+2+3+3 = 10)
# liida sellele a x b x c

fulltotal = 0

with open("file.txt") as f: 
    for item in f:
        list = item.strip()
        stringlist = list.split("x")
        intlist = [eval(i) for i in stringlist]
        intlist.sort()
        a = intlist[0]
        b = intlist[1]
        c = intlist[2]
        wrap = a + a + b + b
        bow = a * b * c
        total = wrap + bow
        fulltotal += total
        print(fulltotal)

