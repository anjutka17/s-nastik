import sõnastik

def kuva_menuu():
    print("\nTere tulemast eesti-vene sõnastikku!")
    print("1 - Tõlgi eesti -> vene")
    print("2 - Tõlgi vene -> eesti")
    print("3 - Lisa uus sõna")
    print("4 - Paranda sõna")
    print("5 - Testi teadmisi")
    print("6 - Kuula sõna (Text-to-Speech)")
    print("7 - Välju")

    while True:
        kuva_menuu()
        valik = input("Tee oma valik: ").strip()
        if valik == '1':
            sõnastik.tolgi_est_rus()
        elif valik == '2':
            sõnastik.tolgi_rus_est()
        elif valik == '3':
            sõnastik.lisa_sona()
        elif valik == '4':
            sõnastik.paranda_sona()
        elif valik == '5':
            sõnastik.testi_teadmisi()
        elif valik == '6':
            sõnastik.text_to_speech()
        elif valik == '7':
            print("Head aega!")
            break
        else:
            print("Tundmatu valik!")
