money = float(input("Cумма, которую Вы планирует положить под проценты?\n"))
t = int(input("Cрок размещения денежных средств (в днях):\n"))
K = int(input("Число дней в году:\n"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int((per_cent['ТКБ']*money*t/K)/100)
SKB = int((per_cent['СКБ']*money*t/K)/100)
VTB = int((per_cent['ВТБ']*money*t/K)/100)
SBER = int((per_cent['СБЕР']*money*t/K)/100)
deposit = [TKB, SKB, VTB, SBER]
print('Накопленные средства в каждом из банков:\nТКБ, СКБ, ВТБ, СБЕР —', deposit)
print('Максимальная сумма, которую Вы можете заработать —', max(deposit))