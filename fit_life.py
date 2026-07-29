# Проект FitLife - MVP версия 1.0


# 1. Знакомство
print('ДОБРО ПОЖАЛОВАТЬ в FitLife!')
print("-" * 45)
print('FitLife помогает заботиться о вашем здоровье!')
# Узнаем имя пользователя
user_name = input('Давай познакомимся, напиши как тебя зовут: ')
# Узнаем возраст пользователя
user_age = int(input('Укажи свой возраст: '))


# 2. Сбор данных
print(f"Отлично, {user_name}!")
print('Мы уже на половине пути к твоей цели!')
print("\n")
# Узнаем ВЕС пользователя в киллограммах
user_weight = float((input('Для нужных расчетов, нам нужно знать твой вес, в'
                           ' (кг): ')))
# Узнаем РОСТ пользователя в метрах
user_height = float((input('Теперь укажи свой рост в метрах, используя точку'
                           ' (например: 1.65): ')))


# 3. Логика расчетов
# ---Расчет ИМТ---
WATER_PER_KG = 30
WATER_L = 1000
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
bmi_result = round(bmi, 1)
# ---Расчет нормы воды---
water_needed = (user_weight * WATER_PER_KG) / WATER_L
water_needed_result = round(water_needed, 1)

# 4. Результат
print("\n" + "-" * 45)
print(f"{user_name}!, вот твой результат!")
print(f"Пользователь: {user_name}, {user_age} г. ")
print(f"Индекс Массы Тела: {bmi_result}")
print(f"Рекомендуемая норма воды: {water_needed_result} л. в день")
print("-" * 45)


print("Расчет окончен. Будьте здоровы!")
