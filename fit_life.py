# Проект FitLife - MVP версия 1.0


class User:
    """Знакомство с новым пользователем
    Атрибуты:
    LINE (constant): обозначает необходимое количество "-", для читаемости
    текста.
    user_name (str): вводит информацию об имени пользователя
    user_age (int): вводит информацию о возрасте пользователя
    """


LINE = "-" * 45


print('ДОБРО ПОЖАЛОВАТЬ в FitLife!')
print(LINE)
print('FitLife помогает заботиться о вашем здоровье!')
user_name = input('Давай познакомимся, напиши как тебя зовут: ')
user_name = user_name.title()
user_age = int(input('Укажи количество полных лет: '))


class Info:
    """Собираем данные о весе и росте для дальнейших расчетов
    Атрибуты:
    user_weight (float): вес в килограммах
    user_height (float): рост в метрах
    Если пользователь ошибется и использует ',', метод .replace() исправляет
    проблему. Обязательно перед (float), так как этот метод используется в
    (str)
    """


print(f"Отлично, {user_name}!")
print('Мы уже на половине пути к твоей цели!')
print("\n")
user_weight = (input('Для нужных расчетов, укажи свой вес, в (кг): '))
user_weight = user_weight.replace(',', '.')
user_weight = float(user_weight)
user_height = (input('Укажи свой рост в метрах, используя точку (например:'
                     ' 1.65): '))
user_height = user_height.replace(',', '.')
user_height = float(user_height)


class Calculation:
    """Производим расчеты Индекса Массы Тела и нормы воды
    Формула ИМТ:
        1)bmi (float): индекс массы тела = user_weight / (user_height ** 2).
        2)bmi_result (float): округляем bmi до 1 цифры после точки с помощью
        round (bmi, 1)

    Формула нормы воды:
        Для расчета потребуется:
        WATER_PER_KG (constant): суточная норма воды в миллилитрах
        WATER_L (constant): 1 литр воды в миллилитрах

    1)water_needed (float): норма воды = (user_weight * WATER_PER_KG) / WATER_L
    2)water_nedeed_result (float): округляем water_needed до 1 цифры после
    точки с помощью round (water_needed, 1)
    """


WATER_PER_KG = 30
WATER_L = 1000


bmi = user_weight / (user_height ** 2)
bmi_result = round(bmi, 1)
water_needed = (user_weight * WATER_PER_KG) / WATER_L
water_needed_result = round(water_needed, 1)


class Result:
    """Выводит пользователю готовый результат"""


print("\n" + LINE)
print(f"{user_name}!, вот твой результат!")
print(f"Пользователь: {user_name}, {user_age} г. ")
print(f"Индекс Массы Тела: {bmi_result}")
print(f"Рекомендуемая норма воды: {water_needed_result} л. в день")
print(LINE)


print("Расчет окончен. Будьте здоровы!")
