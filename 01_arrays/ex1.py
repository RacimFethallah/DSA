expenses = [2200, 2350, 2600, 2130, 2190]


print("1: ", expenses[1] - expenses[0])
print("2: ", expenses[1] + expenses[0] + expenses[2])


print("3: ", 2000 in expenses)
expenses.append(1980)
print("4:", expenses)


expenses[3] = expenses[3] + 200
print("5: ", expenses)
print("6: ", expenses.pop())
