def number_of_pennies(dollars, cents=None):
    dollars_in_cents = dollars*100
    if cents == None:
        cents = 0  
    number_of_pennies = dollars_in_cents + cents
    return number_of_pennies

print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400