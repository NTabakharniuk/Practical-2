
#9) Підрахувати кількість цілих серед чисел а, b, с (ввести з клавіатури).
def count_integers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = 0
    if a.is_integer():
        count += 1
    if b.is_integer():
        count += 1
    if c.is_integer():
        count += 1

    print("Кількість цілих чисел серед a, b, c:", count)

count_integers()