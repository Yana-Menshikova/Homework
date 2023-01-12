per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

x = input('Введите сумму, которую вы хотите положть на депозит:')
y = int(x)
deposit = []

for item in per_cent.items():
    deposit.append(y * item[1] / 100)

max_sum = max(deposit)
print('Максимальная сумма, которую вы можете заработать -', y * test2 / 100)
