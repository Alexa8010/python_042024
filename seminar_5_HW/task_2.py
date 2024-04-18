"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии"""

names = ['Анна', 'Мария', 'Глеб']
rates = [30, 40, 70]
procents = ['10.25%', '6.3%', '9.2%']

result_dict = {name: int(rate * float(procent[:-1]) / 100) 
               for name, rate, procent in zip(names, rates, procents)}

print(result_dict)
