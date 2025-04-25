def loe_failist(failinimi):
    sõnastik = {}
    f = open(failinimi, "r", encoding="utf-8")
    for rida in f:
        rida = rida.strip()
        if ":" in rida:
            est, rus = rida.split(":")
            sõnastik[est] = rus
    f.close()
    return sõnastik

def kirjuta_failisse(failinimi, sõnastik):
    f = open(failinimi, "w", encoding="utf-8")
    for est in sõnastik:
        f.write(est + ":" + sõnastik[est] + "\n")
    f.close()

def tolgi_est_rus(sõnastik):
    sõna = input("Sisesta eesti sõna: ")
    if sõna in sõnastik:
        print("Vene keeles:", sõnastik[sõna])
    else:
        print("Sõna ei leitud!")

def tolgi_rus_est(sõnastik):
    sõna = input("Sisesta vene sõna: ")
    leitud = False
    for est in sõnastik:
        if sõnastik[est] == sõna:
            print("Eesti keeles:", est)
            leitud = True
    if not leitud:
        print("Sõna ei leitud!")

def lisa_sona(sõnastik):
    est = input("Sisesta uus eesti sõna: ")
    rus = input("Sisesta selle tõlge vene keeles: ")
    if est in sõnastik:
        print("See sõna on juba olemas!")
    else:
        sõnastik[est] = rus
        print("Sõna lisatud!")

def paranda_sona(sõnastik):
    est = input("Millist eesti sõna tahad parandada? ")
    if est in sõnastik:
        uus_est = input("Uus eesti sõna: ")
        uus_rus = input("Uus vene sõna: ")
        del sõnastik[est]
        sõnastik[uus_est] = uus_rus
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud!")

def testi_teadmisi(sõnastik):
    punktid = 0
    kokku = 3
    loetelu = list(sõnastik.items())
    for i in range(min(kokku, len(loetelu))):
        est, rus = loetelu[i]
        vastus = input("Mis on vene keeles: " + est + "? ")
        if vastus == rus:
            print("Õige!")
            punktid += 1
        else:
            print("Vale. Õige vastus oli:", rus)
        print("Said", punktid, "punkti", "/", kokku)