barcode = input("sisesta vöötkood: ")

sum_odd = 0
for i in range(0,12, 2):
    sum_odd += int(barcode[i])
    
sum_odd *= 3

sum_even = 0
for i in range(1,10,2):
    sum_even += int(barcode[i])

sum_all = sum_odd + sum_even

m = sum_all % 10

if m != 0:
    print("kontrollsumma: ", 10 - m)