import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}


wall_height = float(input('Enter wall height (feet): \n'))
wall_width = float(input('Enter wall width (feet): \n'))

wall_area = wall_height * wall_width

print('Wall area:',wall_area,'square feet')
   
paint_needed = wall_area / 350   
print('Paint needed:',paint_needed,'gallons')

cans_needed = math.ceil(paint_needed)

print('Cans needed:',cans_needed,'can(s)''\n')

print('Choose a color to paint the wall: ')

paintCost = {'red':35,'blue':75}
paintColor = input()

print('Cost of purchasing ',paintColor,' paint: $',paintCost[paintColor],sep='')