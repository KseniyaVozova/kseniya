salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital=0
a=0
b=0
for x in range(1,11):
    if x==1:
        capital = spend-salary
        a +=capital
    else:
        spend=spend+spend*increase
        capital=spend-salary
        b +=capital
capital=a+b
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital,2))
