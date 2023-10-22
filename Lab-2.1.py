money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
new_spend = spend * (1 + increase)
months = 0
while money_capital >= 0:
    if months == 0:
        money = salary - spend
    else:
        money = salary - new_spend
    new_spend *= 1 + increase
    months += 1
    money_capital += money

print("Количество месяцев, которое можно протянуть без долгов:", months-1)
