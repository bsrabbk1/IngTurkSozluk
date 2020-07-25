

import os

kelimeler = {
	
	"get":["Almak","Edinmek","Olmak","Elde etmek"],
	"break":["Ara","Kırılma","Fren"],
	"good":["İyi","Güzel"],
	"winner":["Galip","Kazanan","Birinci"],
	"easy":["Kolay","Basit","Zahmetsiz"]


}

def kelimeEkle(kelime,kelimeler):
	if kontrol(kelime,kelimeler):
		mevcut_anlamlar = set(kelimeler[kelime])
		yeni_giris = input("Kelime mevcut. Girdiğiniz kelimenin kayıtlı anlamları: {}\n Yeni bir anlam girmek ister misiniz?(H/E)".format(mevcut_anlamlar))
		if yeni_giris.lower()=="e":
			yeni_anlam= input ("Girmek istediğiniz anlamları aralarına virgül koyarak yazınız: ")
			yeni_anlamları_böl= set(yeni_anlam.split(","))
			kelimeler[kelime]= list(mevcut_anlamlar | yeni_anlamları_böl)
			print("Girdiğiniz anlamlar kaydedildi. Anlamlar listesinin son hali: ",kelimeler[kelime])
		elif yeni_giris.lower()== "h":
			pass
	else:
		yeni_anlam= input("Girmek istediğiniz anlamları aralarına virgül koyarak yazınız: ")
		yeni_anlamları_böl= set(yeni_anlam.split(","))
		kelimeler[kelime]= list( yeni_anlamları_böl)
		print("Girdiğiniz anlamlar kaydedildi. Anlamlar listesinin son hali: ",kelimeler[kelime])
	input("Devam etmek için bir tuşa basın.")


def kelimeÇevir(kelime,kelimeler):
	if kontrol(kelime,kelimeler):
		print("{} kelimesinin anlamları ".format(kelime),end=": ")
		print(*kelimeler[kelime])
	else:
		print("Girdiğiniz kelime mevcut değil")
	input("Devam etmek için bir tuşa basın.")



def kontrol(kelime,kelimeler):
	if kelime in kelimeler:
		return True
	else:
		return False





def kelimeleriListele():
	for no,kelime in enumerate (kelimeler,1):
		print("{}.{}".format(no,kelime))
	input("Devam etmek için bir tuşa basın.")
#kelimeleriListele()


secenekler= """

	[1] Kelime Ekle
	[2] Kelime Çevir
	[3] Kelimeleri Listele


"""
while True:
	temizle= ("cls" if os.name== "nt" else "clear")
	os.system(temizle)
	print(secenekler)
	secenek= int(input("Seçiminizi yapınız: "))

	if secenek == 1:
		kelime= input("Eklenecek ingilizce kelimeyi giriniz: ")
		kelimeEkle(kelime,kelimeler)
	elif secenek == 2:
		kelime= input("Anlamını öğrenmek istediğiniz ingilizce kelimeyi giriniz: ")
		kelimeÇevir(kelime,kelimeler)
	elif secenek== 3:
		kelimeleriListele()