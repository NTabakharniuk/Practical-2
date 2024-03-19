
#6)Увести з клавіатури цілі числа a, b. Якщо числа не рівні, то замінити кожне з них одним і тим же числом, рівним більшому із вихідних, а якщо рівні, то замінити числа нулями.
def replace_numbers():

    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))

    if a != b:
        max_num = max(a, b)
        a = max_num
        b = max_num
    else:
        a = 0
        b = 0

    print("Результат заміни:")
    print("a =", a)
    print("b =", b)

replace_numbers()
