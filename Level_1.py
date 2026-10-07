import math

x1, y1 = map(float, input("Введіть координати A (x y): ").split())
x2, y2 = map(float, input("Введіть координати B (x y): ").split())
x3, y3 = map(float, input("Введіть координати C (x y): ").split())
x4, y4 = map(float, input("Введіть координати D (x y): ").split())

if (x1 + x3 == x2 + x4) and (y1 + y3 == y2 + y4):

    AB = (x2 - x1, y2 - y1)
    AD = (x4 - x1, y4 - y1)

    S = abs(AB[0] * AD[1] - AB[1] * AD[0])

    if S == 0:
        print("Помилка: точки не утворюють паралелограм.")
    else:
        AC = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        BD = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)

        print(f"\nПлоща паралелограма: {S:.3f}")
        print(f"Довжина діагоналі AC: {AC:.3f}")
        print(f"Довжина діагоналі BD: {BD:.3f}")

else:
    print("Помилка: введені точки не утворюють паралелограм.")