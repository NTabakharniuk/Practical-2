
#8) Підрахувати кількість додатних серед чисел а, b, с (ввести з клавіатури).
def count_positives():

    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1

    print("Кількість додатних чисел серед a, b, c:", count)

count_positives()