class Ogrenci:

    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


    #Öğrenci bilgilerinin doğru kaydedildiğini teyit etmek için:
    def ogrenci_bilgisi(self):
        return self.ogrenci_adi + " " + self.ogrenci_soyadi + " " + self.ogrenci_sinif



class Soru:

    def __init__(self):
        pass

    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        self.dogru_sayisi = dogru_sayisi
        self.yanlis_sayisi = yanlis_sayisi

        net_sayisi = dogru_sayisi - yanlis_sayisi * 0.25

        return net_sayisi

    def hesapla(self, net_sayisi):
        self.net_sayisi = net_sayisi

        score = net_sayisi * 2

        return score


ogr1 = Ogrenci(input("Ogrenci adini girin: "), input("Ogrenci soyadini girin: "), input("Ogrenci sinifini girin: "))
print(ogr1.ogrenci_bilgisi())

score1 = Soru.net_sayisi()






