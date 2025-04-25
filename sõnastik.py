import random

# eesti-vene sõnastik
sõnastik = {
'koer': 'собака',
'kass': 'кошка',
'maja': 'дом',
'auto': 'машина',
'päike': 'солнце'
}

def tolgi_est_rus():
	sõna = input("Sisesta sõna eesti keeles: ").lower()
	if sõna in sõnastik:
		print("Vene keeles:", sõnastik[sõna])
	else:
		print("Sõna ei leitud!")

def tolgi_rus_est():
	sõna = input("Sisesta sõna vene keeles: ").lower()
	found = False
	for est, rus in sõnastik.items():
		if rus == sõna:
			print("Eesti keeles:", est)
			found = True
		break
	if not found:
			print("Sõna ei leitud!")

def lisa_sona():
	est = input("Sisesta uus sõna eesti keeles: ").lower()
	rus = input("Sisesta selle sõna vene tõlge: ").lower()
	if est in sõnastik:
		print("Sõna on juba olemas!")
	else:
		sõnastik[est] = rus
		print("Sõna lisatud!")

def paranda_sona():
	vana = input("Sisesta parandatav eesti sõna: ").lower()
	if vana in sõnastik:
		uus_est = input("Sisesta uus eesti sõna: ").lower()
		uus_rus = input("Sisesta uus vene tõlge: ").lower()
		del sõnastik[vana]
		sõnastik[uus_est] = uus_rus
		print("Sõna parandatud!")
	else:
		print("Sõna ei leitud!")

def testi_teadmisi():
	suund = input("Vali suund (1 = eesti → vene, 2 = vene → eesti): ")
	punktid = 0
	kokku = 3
	sõnad = list(sõnastik.items())
	random.shuffle(sõnad)

	for i in range(kokku):
		est, rus = sõnad[i]
		if suund == '1':
			vastus = input(f"Sõna '{est}' vene keeles: ").lower()
			if vastus == rus:
				print("Õige!")
				punktid += 1
			else:
				print(f"Vale! Õige vastus: {rus}")
		elif suund == '2':
			vastus = input(f"Sõna '{rus}' eesti keeles: ").lower()
			if vastus == est:
				print("Õige!")
				punktid += 1
			else:
				print(f"Vale! Õige vastus: {est}")
				protsent = punktid / kokku * 100
				print(f"Sinu tulemus: {protsent:.0f}%")
	

