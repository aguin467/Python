weight1 = float(input("Enter weight 1: "))
print('')
weight2 = float(input("Enter weight 2: "))
print('')
weight3 = float(input("Enter weight 3: "))
print('')
weight4 = float(input("Enter weight 4: "))
print('')
print('')


weights = []
weights.append(weight1)
weights.append(weight2)
weights.append(weight3)
weights.append(weight4)


print("Weights:", weights)


total = 0
for weight in weights:
    total += weight
average = total/4
print("Average weight:", "{0:.2f}".format(average))


print("Max weight:", "{0:.1f}".format(max(weights)))
print('')


index = int(input("Enter a list index (1 - 4): ")) - 1
print('')

print("Weight in pounds:", weights[index])
print("Weight in kilograms:", "{0:.1f}".format(weights[index]/2.2))
print('')


weights.sort()
print("Sorted list:", weights)
