
# 5) На площині ХОY задана своїми координатами точка А (координати ввести з клавіатури). Вказати, де вона розташована (на якій осі або в якому координатном куті)
def point_location():

    x = float(input("Введіть координату x для точки: "))
    y = float(input("Введіть координату y для точки: "))

    if x == 0 and y == 0:
        print("Точка розташована в початку координат.")
    elif x == 0:
        print("Точка розташована на осі Y.")
    elif y == 0:
        print("Точка розташована на осі X.")
    elif x > 0 and y > 0:
        print("Точка розташована в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка розташована в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка розташована в третьому квадранті.")
    else:
        print("Точка розташована в четвертому квадранті.")

point_location()