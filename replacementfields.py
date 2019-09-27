print('The {animal} in the {headwear}'.format(animal='Cat',headwear='Fedora'))



animal = input()
headwear = input()

print('The Big %s' % animal,headwear)

num_of_kids = int(input())
kids_name = input()

print('The number of kids that {1} has is {0}:'.format(num_of_kids,kids_name))

if(len(str(kids_name >= '5'))):
    print(len(str(kids_name)))
else:
   print('Error!')
