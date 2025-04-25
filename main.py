import sõnastik

fail = "sõnastik.txt"
sõnad = sõnastik.loe_failist(fail)

def kuva_menuu():
    print("\n--- Eesti-Vene sõnastik ---")
    print("1 - Tõlgi eesti -> vene")
    print("2 - Tõlgi vene -> eesti")
    print("3 - Lisa uus sõna")
    print("4 - Paranda sõna")
    print("5 - Testi teadmisi")
    print("6 - Välju")

while True:
    kuva_menuu()
    valik = input("Vali tegevus (1-6): ")
    if valik == "1":
        sõnastik.tolgi_est_rus(sõnad)
    elif valik == "2":
        sõnastik.tolgi_rus_est(sõnad)
    elif valik == "3":
        sõnastik.lisa_sona(sõnad)
        sõnastik.kirjuta_failisse(fail, sõnad)
    elif valik == "4":
        sõnastik.paranda_sona(sõnad)
        sõnastik.kirjuta_failisse(fail, sõnad)
    elif valik == "5":
        sõnastik.testi_teadmisi(sõnad)
    elif valik == "6":
        print("Head aega!")
        break
    else:
        print("Vale valik!")

# чтобы окно не закрылось сразу
input("\nVajuta Enter, et väljuda...")