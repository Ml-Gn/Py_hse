number = input("Введите число, а мы превратим его в четверку: ")
true_number = int(number)
print("Сначала умножим на два, получим ", (true_number*2))
print("Прибавим к результату 8, получим ", ((true_number*2)+8))
print("Разделим результат на 2, получим ", ((((true_number*2)+8)//2)))
print("А теперь вычтем загаданное Вами число и получим...", ((((true_number*2)+8)//2 - true_number)))

testing commit n git