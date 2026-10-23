import math

print("Вариант 1. Расчёт скорости резания при токарной обработке")
print("Меню:")
print("1 - черновая обработка (k = 1.0)")
print("2 - получистовая (k = 0.85)")
print("3 - чистовая (k = 0.7)")

# Выбор режима обработки (match-case)
choice = input("Выберите режим (1-3): ").strip()

match choice:
    case "1":
        mode = "черновая обработка"
        k = 1.0
    case "2":
        mode = "получистовая обработка"
        k = 0.85
    case "3":
        mode = "чистовая обработка"
        k = 0.7
    case _:
        print("Ошибка: неверный пункт меню, нужно ввести 1, 2 или 3.")
        raise SystemExit

# Ввод данных с проверкой допустимых диапазонов
try:
    D = float(input("Диаметр заготовки D, мм (1..500): ").replace(",", "."))
    n = float(input("Частота вращения n, об/мин (50..3000): ").replace(",", "."))
except ValueError:
    print("Ошибка: нужно вводить числа.")
    raise SystemExit

if not (1 <= D <= 500):
    print("Ошибка: диаметр должен быть в диапазоне 1..500 мм.")
    raise SystemExit
if not (50 <= n <= 3000):
    print("Ошибка: частота вращения должна быть в диапазоне 50..3000 об/мин.")
    raise SystemExit

# Расчёт
V = math.pi * D * n / 1000      # м/мин
V_adj = V * k

# Классификация диаметра (if-elif-else)
if D < 10:
    diameter_class = "малый диаметр"
elif D <= 100:
    diameter_class = "нормальный диаметр"
else:
    diameter_class = "крупный диаметр"

# Вывод
print()
print(f"Режим: {mode}")
print(f"V = {V:.2f} м/мин")
print(f"V_adj = {V_adj:.2f} м/мин")
print(f"Класс диаметра: {diameter_class}")