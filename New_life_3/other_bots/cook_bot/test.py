list_remote = [3, 7, 11]
list_number = [5, 4, 3, 90, 24, 2, 7, 67, 12, 11, 'lion']

for i in range(len(list_remote)):
    list_number.remove(list_remote[i])
    print(list_number)
