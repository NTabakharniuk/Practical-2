#10) Визначити, дільником яких чисел а, b, с є число k (ввести з клавіатури).
def find_divisor():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    c = int(input("Введіть число c: "))
    k = int(input("Введіть число k: "))

    if a % k == 0:
        print(k, "є дільником числа a")
    else:
        print(k, "не є дільником числа a")

    if b % k == 0:
        print(k, "є дільником числа b")
    else:
        print(k, "не є дільником числа b")

    if c % k == 0:
        print(k, "є дільником числа c")
    else:
        print(k, "не є дільником числа c")

find_divisor()
