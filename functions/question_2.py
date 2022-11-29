# sayi_atama ve sayi_okunusu isimli 2 tane fonksiyon tanımlayınız.
# Bu fonksiyonlardan sayi_atama fonksiyonu 2 basamaklı bir sayıyı parametre olarak alsın ve
# fonksiyon içinde bu değer bir değişkene atansın.
# Daha sonra sayi_atama fonksiyonu içinde sayi_okunusu isimli fonksiyon çağırılarak
# değişkene atanan sayının okunuşu string olarak verilsin.
# sayi_atama fonksiyonu 2 basamaktan daha az yada daha fazla sayıyı kabul etmeyecektir.

"""
Bu ödev key-value dizileri araştırılarak tekrar yapılacak
"""
birler = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}
onlar = {1: "on ", 2: "yirmi ", 3: "otuz ", 4: "kırk ", 5: "elli ", 6: "altmış ", 7: "yetmiş ", 8: "seksen ", 9: "doksan "}

input_number = int(input("Please enter a number: "))


def sayi_okunusu(okunacak_sayi):
    final_string = ""
    okunacak_sayi = str(okunacak_sayi)
    first_char = int(okunacak_sayi[0])
    second_char = int(okunacak_sayi[1])
    if second_char == 0:
        final_string += onlar[first_char]
    else:
        final_string += onlar[first_char]
        final_string += birler[second_char]
    print(final_string)


def sayi_atama(input_number):
    if input_number < 10 or input_number > 99:
        print("The number cannot be less than 10 or greater than 99. Please try again.")
        quit()
    sayi_okunusu(input_number)


sayi_atama(input_number)