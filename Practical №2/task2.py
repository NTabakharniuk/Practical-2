#2) Увести з клавіатури координати двох точок А (х1, у1) і В (х2, у2). Скласти алгоритм, який визначає, яка з точок знаходиться ближче до початку координат.
def closer_point():
    x1 = float(input("Введіть координату x для точки A: "))
    y1 = float(input("Введіть координату y для точки A: "))
    x2 = float(input("Введіть координату x для точки B: "))
    y2 = float(input("Введіть координату y для точки B: "))

    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance1 < distance2:
        print("Точка A знаходиться ближче до початку координат.")

    elif distance2 < distance1:
        print("Точка B знаходиться ближче до початку координат.")

    else:
        print("Обидві точки знаходяться на однаковій відстані від початку координат.")

closer_point()