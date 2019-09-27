team = {}

#jersey = 1
#rating = 1

i = 1

for i in range(1, 6):
  jersey = int(input('Enter player {}\'s jersey number:\n' .format(i)))
  rating = int(input('Enter player {}\'s rating:\n' .format(i)))
  if jersey < 0 and jersey > 99 and rating < 0 and rating > 9:
    print('invalid entry')
    break
  else:
    team[jersey] = rating

print('\nROSTER')
sorted_roster = sorted(team.keys())
for jersey in sorted_roster:
    print('Jersey number: {}, Rating: {}' .format(jersey, rating))

print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')

menu_option = input('You\'ve got options:\n')

if menu_option == 'a':
  jersey = int(input('Enter a new player\'s jersey number:\n' .format(i)))
  rating = int(input('Enter the players\'s rating:' .format(i)))
  team[jersey] = rating

elif menu_option == 'd':
  jersey = int(input('Enter a jersey number:'))
  if jersey in team.keys():
    del team[jersey]

elif menu_option == 'u':
  jersey = int(input('Enter a jersey number: '))
  if jersey in team.keys():
    rating = int(input('Enter a new rating for player: '))
    team[jersey] = rating

elif menu_option == 'r':
  print('ABOVE {}'.format(rating))
  sorted_roster = sorted(team.keys())
  if team[jersey] > rating:
    print('Enter a rating:')
