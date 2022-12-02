#3 tane parametre alan bolunen_sayi_bulma isimli bir fonksiyon tanımlayınız.
#Bu fonsiyon; min_sayi, max_sayi, bolen_sayi isimli parametreleri alsın.
#Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak, min_sayi ve max_sayi
#aralığındaki bolen_sayi değerine bölünen sayıları tam_bolunenler adlı bir diziye atayıp, listelesin.
#tam_bolunenler dizisi ile min_sayi ve max_sayi arasındaki değerlerin sayısını return ile döndürsün.

tam_bolunenler = []
min_sayi = int(input("Minimum sayı değerini girin: "))
max_sayi = int(input("Maximum sayı değerini girin: "))
bolen_sayi = int(input("Bölen sayı değerini girin: "))


def bolunen_sayı_bulma(min_sayi, max_sayi, bolen_sayi):
    for her_sayi in range(min_sayi, max_sayi + 1):
        if her_sayi % bolen_sayi == 0:
            tam_bolunenler.append(her_sayi)

    return tam_bolunenler


print(bolunen_sayı_bulma(min_sayi, max_sayi, bolen_sayi))
