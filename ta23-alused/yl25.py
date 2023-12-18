# Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
# Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
# Muuda magustoidu väärtust.
# Tee kordus üle dictionary ja väljasta kõik võtmed.
# Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
# Kontrolli, kas isikukood on dictionary's olemas.
# Leia dictionary suurus (elementide arv).
# Lisa element enda pikkuse jaoks.
# Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
# Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
# Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
# Tutvu kõigi dictionary meetoditega.
# Läbi ülesanne juhendi lõpus.

dict = {
    "eesnimi" : "henrik",
    "perenimi" : "mütt",
    "sünniaasta" : 1996,
    "elukoht" : "kuressaare",
    "magustoit" : "kana"
}

print(dict["elukoht"])

x = dict.get("elukoht")
print(x)

dict.update({"magustoit" : "siga"})
print(dict)