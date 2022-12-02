"""
Insan isimli bir sınıf tanımlayınız.

Bütün constructor parametreleri default değerlere sahip olacak, default contructor (__init__) içinde belirlenecektir.

Bu değerler; ad, soyad, yas, ulke, sehir olacaktır.
Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacaktır.

kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le döndürülecektir.

yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecektir.

Bu classtan belirtilen bilgileri içeren bir nesne tanımlayınız.

Tanımlanan nesneye yetenek ekleyiniz. (Bisiklete binmek, Python vs.)

kisi_bilgileri fonksiyonu ile bu bilgileri console ekranında gösteriniz.
"""


class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = str(yas)
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        kisi_bilgileri = self.ad + " " + self.soyad + " " + self.yas + " " + self.ulke + " " + self.sehir + " "

        for her_yetenek in self.yetenekler:
            kisi_bilgileri += her_yetenek + " "

        return kisi_bilgileri

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


insan1 = Insan("furkan", "tök", 22, "tr", "ist")
insan1.yetenek_ekle("bisiklet binmek")
insan1.yetenek_ekle("python")
print(insan1.kisi_bilgileri())

