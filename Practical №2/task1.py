# 1)Увести з клавіатури три дійсних числа. Піднести до квадрата ті з них, значення яких невід'ємні, і в четверту ступінь - від`ємні .
def calculate_numbers():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    num3 = float(input("Введіть третє число: "))

    if num1 >= 0:
        result1 = num1 ** 2
    else:
        result1 = num1 ** 4

    if num2 >= 0:
        result2 = num2 ** 2
    else:
        result2 = num2 ** 4

    if num3 >= 0:
        result3 = num3 ** 2
    else:
        result3 = num3 ** 4

    print("Результат першої задачі:", [result1, result2, result3])

calculate_numbers()