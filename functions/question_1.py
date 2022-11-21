#3 tane parametre alan bolunen_sayi_bulma isimli bir fonksiyon tanımlayınız.
#Bu fonsiyon; min_sayi, max_sayi, bolen_sayi isimli parametreleri alsın.
#Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak, min_sayi ve max_sayi
#aralığındaki bolen_sayi değerine bölünen sayıları tam_bolunenler adlı bir diziye atayıp, listelesin.
#tam_bolunenler dizisi ile min_sayi ve max_sayi arasındaki değerlerin sayısını return ile döndürsün.

tam_bolunenler = []

min_input = int(input("Minimum sayı değerini girin: "))
max_input = int(input("Maximum sayı değerini girin: "))
bolen_input = int(input("Bölen sayı değerini girin: "))

def bolunen_sayı_bulma(min_sayi = min_input, max_sayi = max_input, bolen_sayi = bolen_input):
    for her_sayi in range(min_sayi, max_sayi + 1):
        if her_sayi % bolen_sayi == 0:
            tam_bolunenler.append(her_sayi)

    print(tam_bolunenler)

bolunen_sayı_bulma()
