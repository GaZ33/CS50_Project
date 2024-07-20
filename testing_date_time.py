
from datetime import timedelta, date, datetime

teste = datetime.now()

"""

a = teste.day

a = a+7

b = datetime.date(teste)
date1 =timedelta.days(1)
print(date1)
dateteste = date1
print(b)
"""
a = 7
teste = teste.replace(day=teste.day+a)
print(teste)
