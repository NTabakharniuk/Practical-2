
#7) Підрахувати кількість негативних серед чисел а, b, с (ввести з клавіатури)
def count_negatives():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1

    print("Кількість негативних чисел серед a, b, c:", count)

count_negatives()