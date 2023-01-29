stringNumbers = ""
listNumbers = []
randomNumber = 0
flag1 = True
flag2 = True


def BubleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    num = -1
    result = []

    while low <= high:
        middle = (low + high) // 2

        if data[middle] == elem:
            num = elem
            break
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    if num == -1:
        if high == -1:
            result.append(0)
            print("Номера позиции меньшего числу из условия не существует!")
        else:
            result.append(high)
            try:
                nextIndex = data[high + 1]
                result.append(high + 1)
            except IndexError:
                print("Номера позиции большего или равного числу из условия не существует!")
    else:
        index = data.index(num)
        if index != 0:
            result.append(index - 1)
        else:
            print("Номера позиции меньшего числу из условия не существует!")
        result.append(index)

    return result


while flag1:
    listNumbers = []
    flag1 = False
    stringNumbers = input("Введите числа через пробел:\n")
    stringNumbers = stringNumbers.strip()
    listStrin = stringNumbers.split(" ")

    for item in listStrin:
        try:
            newElement = int(item)
            listNumbers.append(newElement)
        except ValueError:
            print("Введен неправильный формат данных! \n")
            flag1 = True
            break

while flag2:
    flag2 = False
    oneNumber = input("Введите любое число:\n")

    try:
        randomNumber = int(oneNumber)
    except ValueError:
        print("Введен неправильный формат данных! \n")
        flag2 = True

sortListNumbers = BubleSort(listNumbers)
print("Позиции соответствующие условию задачи:", binary_search(sortListNumbers, randomNumber))
