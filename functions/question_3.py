# Kullanıcının girdiği vize1, vize2, final notlarına göre harf notunu hesaplayınız.
# -vize1 toplam notun %30'una etki edecektir.
# -vize2 toplam notun %30'una etki edecektir.
# -final toplam notun %40'ına etki edecektir.

#    Toplam Not >=  90 -----> AA
#    Toplam Not >=  85 -----> BA
#    Toplam Not >=  80 -----> BB
#    Toplam Not >=  75 -----> CB
#    Toplam Not >=  70 -----> CC
#    Toplam Not >=  65 -----> DC
#    Toplam Not >=  60 -----> DD
#    Toplam Not >=  55 -----> FD
#    Toplam Not <  55 -----> FF

def not_kontrol(sinav):
    if sinav < 0 or sinav > 100:
        print("Lütfen geçerli bir sınav notu girin. Sınav notu 0'dan küçük ya da 100'den büyük olamaz.")
        quit()


vize1 = int(input("Birinci vize notunu giriniz: "))
vize1_yüzde = vize1 * 30 / 100
not_kontrol(vize1)

vize2 = int(input("İkinci vize notunu giriniz: "))
vize2_yüzde = vize2 * 30 / 100
not_kontrol(vize2)

final = int(input("Final sınavı notunuzu giriniz: "))
final_yüzde = final * 40 / 100
not_kontrol(final)

toplam_not = int(vize1_yüzde + vize2_yüzde + final_yüzde)

if toplam_not >= 90:
    print(f"Notunuz {toplam_not}: AA")
elif toplam_not >= 85:
    print(f"Notunuz {toplam_not}: BA")
elif toplam_not >= 80:
    print(f"Notunuz {toplam_not}: BB")
elif toplam_not >= 75:
    print(f"Notunuz {toplam_not}: CB")
elif toplam_not >= 70:
    print(f"Notunuz {toplam_not}: CC")
elif toplam_not >= 65:
    print(f"Notunuz {toplam_not}: DC")
elif toplam_not >= 60:
    print(f"Notunuz {toplam_not}: DD")
elif toplam_not >= 55:
    print(f"Notunuz {toplam_not}: FD")
else:
    print(f"Notunuz {toplam_not}: FF")
