# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks.
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi.
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida.
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

# Küsi kasutajalt kolme külje pikkuseid
# kontrolli, kas sellist kolmnurka saab üldse eksisteerida
# tee selgeks, kas tegemist on erikülgse, võrdhaarse või võrdkülgse kolmnurgaga

ab = float(input("Sisesta 1. külg (cm): "))
ac = float(input("Sisesta 2. külg (cm): "))
bc = float(input("Sisesta 3. külg (cm): "))


if ab == ac and ab == bc:
    print("Võrdkülgne kolmnurk")

elif ab == ac or ab == bc or ac == bc:
    print("võrdhaarne kolmnurk")

else:
    print("Eriküljeline kolmnurk")

if ab + ac < bc or ac + bc < ab or bc + ab < ac:
    print("Sellist kolmnurka pole olemas!")