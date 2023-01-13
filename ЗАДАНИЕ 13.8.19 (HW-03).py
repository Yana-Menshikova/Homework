tickets = int(input("Введите количество билетов: "))

age_list = []
amount = 0
result = 0

counter = 0
while counter < tickets:
    age = int(input(f"Введите возраст для билета № {counter + 1}:"))
    age_list.append(age)
    counter += 1

for age in age_list:
    if age >= 18 and age <= 25:
        amount += 990
    if age > 25:
        amount += 1390

if tickets > 3:
    result = amount / 100 * 90
else:
    result = amount

print(f"Стоимость Вашего заказа: {result}")
