# Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

# defineeri, mis on millest tugevam
# Loopi mängu senikaua, kui kasutaja ei taha enam mängida - küsi peale igat korda, kas tahab mängida või ei taha - kui jah, Loop jätkub, kui ei, siis Loop lõpeb

# "kivi" > "käärid"
# "käärid" > "paber"
# "paber" > "kivi"

import random
game = ["kivi", "paber", "käärid"]

while True:
    computer = random.choice(game)
    player = input("kivi, paber või käärid: ")

    print("Sina: ", player)
    print("Arvuti:", computer)

    if player == computer:
        print("Jäite viiki!")
    elif player == "kivi":
        if computer == "käärid":
            print("Sina võitsid")
        else:
            print("Kaotasid!")
    elif player == "käärid":
        if computer == "paber":
            print("Sina võitsid!")
        else:
            print("Kaotasid!")
    elif player == "paber":
        if computer == "kivi":
            print("Sina võitsid")
        else:
            print("Kaotasid!")

    c = input("Kas soovid jätkata?: ")

    if c == "jah":
        continue
    else:
        print("Mängime varsti jälle!")
        break
        











        








   


