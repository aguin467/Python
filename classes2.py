class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable) #Takes the value of the variable named variable and inputs it into myobjectx. 
# It also stores the function in this variable called myobjectx and it goes back to the class MyClass.

print(myobjecty.variable)
# This is the same as myobjecty but instead it is given "yackity" for the variable value.