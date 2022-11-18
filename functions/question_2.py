# sayi_atama ve sayi_okunusu isimli 2 tane fonksiyon tanımlayınız.
# Bu fonksiyonlardan sayi_atama fonksiyonu 2 basamaklı bir sayıyı parametre olarak alsın ve
# fonksiyon içinde bu değer bir değişkene atansın.
# Daha sonra sayi_atama fonksiyonu içinde sayi_okunusu isimli fonksiyon çağırılarak
# değişkene atanan sayının okunuşu string olarak verilsin.
# sayi_atama fonksiyonu 2 basamaktan daha az yada daha fazla sayıyı kabul etmeyecektir.

def sayi_okunusu(okunacak_sayi):
    okunacak_sayi = str(okunacak_sayi)
    first_char = int(okunacak_sayi[0])
    second_char = int(okunacak_sayi[1])

    final_string = ""
    if first_char == 1:
        final_string += "on "
    elif first_char == 2:
        final_string += "yirmi "
    elif first_char == 3:
        final_string += "otuz "
    elif first_char == 4:
        final_string += "kırk "
    elif first_char == 5:
        final_string += "elli "
    elif first_char == 6:
        final_string += "altmış "
    elif first_char == 7:
        final_string += "yetmiş "
    elif first_char == 8:
        final_string += "seksen "
    elif first_char == 9:
        final_string += "doksan "

    if second_char == 0:
        if first_char == 1:
            final_string = "on"
        elif first_char == 2:
            final_string = "yirmi"
        elif first_char == 3:
            final_string = "otuz"
        elif first_char == 4:
            final_string = "kırk"
        elif first_char == 5:
            final_string = "elli"
        elif first_char == 6:
            final_string = "altmış"
        elif first_char == 7:
            final_string = "yetmiş"
        elif first_char == 8:
            final_string = "seksen"
        elif first_char == 9:
            final_string = "doksan"
    elif second_char == 1:
        final_string += "bir"
    elif second_char == 2:
        final_string += "iki"
    elif second_char == 3:
        final_string += "üç"
    elif second_char == 4:
        final_string += "dört"
    elif second_char == 5:
        final_string += "beş"
    elif second_char == 6:
        final_string += "altı"
    elif second_char == 7:
        final_string += "yedi"
    elif second_char == 8:
        final_string += "sekiz"
    elif second_char == 9:
        final_string += "dokuz"
    print(final_string)

input_number = int(input("Please enter a number: "))

def sayi_atama(number = input_number):
    if number < 10 or number > 99:
        print("The number cannot be less than 10 or greater than 99. Please try again.")
        quit()
    sayi_okunusu(number)
sayi_atama()