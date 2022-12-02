"""
50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen doğru yanlış sayısına göre
aldığı puanı hesaplayan programı yazınız.

Ogrenci isimli bir sınıf tanımlayınız.

Bu sınıfın içinde ogrenci_adi, ogrenci_soyadi, ogrenci_sinif’ı değişkenleri bulunacaktır.
Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecektir.

Soru diye bir sınıfınız olacaktır. Bu sınıfın net_sayisi ve hesapla isimli iki fonksiyon olacaktır.

net_sayisi fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulacaktır.

hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacaktır.
Her net 2 puan olacak şekilde öğrenci bilgileri ve puanı console ekranında gösterilecektir.
"""


class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


class Soru:
    def __init__(self):
        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0

    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        for _ in range(yanlis_sayisi):
            dogru_sayisi -= 0.25

        return dogru_sayisi

    def hesapla(self, dogru_sayisi):
        final_not = dogru_sayisi * 2

        return final_not


ogrenci1 = Ogrenci("furkan", "tök", "a")
final_notu = Soru()
print(final_notu.hesapla(final_notu.net_sayisi(40, 10)))
