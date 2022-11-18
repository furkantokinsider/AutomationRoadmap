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

vize1 = int(input("Please enter your first mid-term grade: "))
midterm1_percentage = vize1 * 30 / 100

vize2 = int(input("Please enter your second mid_term grade: "))
midterm2_percentage = vize2 * 30 / 100

final = int(input("Please enter your final exam grade: "))
final_percentage = final * 40 / 100

total_grade = int(midterm1_percentage + midterm2_percentage + final_percentage)

if total_grade >= 90:
    print(f"Your grade is {total_grade}: AA")
elif total_grade >= 85:
    print(f"Your grade is {total_grade}: BA")
elif total_grade >= 80:
    print(f"Your grade is {total_grade}: BB")
elif total_grade >= 75:
    print(f"Your grade is {total_grade}: CB")
elif total_grade >= 70:
    print(f"Your grade is {total_grade}: CC")
elif total_grade >= 65:
    print(f"Your grade is {total_grade}: DC")
elif total_grade >= 60:
    print(f"Your grade is {total_grade}: DD")
elif total_grade >= 55:
    print(f"Your grade is {total_grade}: FD")
elif total_grade < 55:
    print(f"Your grade is {total_grade}: FF")
