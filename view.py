# view.py

def get_user_input():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите операцию (+, -, *, /, **): ")
    num2 = float(input("Введите второе число: "))
    return num1, operator, num2

def display_result(result):
    print(f"Результат: {result}")


def get_user_input_figure():
    side1 = float(input("Введите первую сторону: "))
    figure = input('Выберите фигуру (triangle, sircle, rectangle)')
    side2 = float(input("Введите вторую сторону: "))
    side3 = float(input("Введите третью сторону: "))
    side4 = float(input("Введите четвёртую сторону: "))
    radius = float(input("Введите радиус: "))
    return semi-perimeter, radius, side4, side3, side2, figure, side1