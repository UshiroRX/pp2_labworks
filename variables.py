#Example 
x = 5
y = "John"
print(x)
print(y)

#Example 
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Example 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Example
x = 5
y = "John"
print(type(x))
print(type(y))

#Example
x = "John"
# is the same as
x = 'John'

#Example
a = 4
A = "Sally"
#A will not overwrite a

#Example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example
2myvar = "John"
my-var = "John"
my var = "John"

myVariableName = "John" #Camel case
MyVariableName = "John" #Pascal case
my_variable_name = "John" #Snake case

#Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Example
x = "Python is awesome"
print(x)

#Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Exmaple
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example
x = 5
y = 10
print(x + y)

#Example
x = 5
y = "John"
print(x + y)

#Example
x = 5
y = "John"
print(x, y)

#Example
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#Example
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Example
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Exercise 1
carname = "Volvo"

# Exercise 2
x = 50

# Exercise 3
x = 5
y = 10
print(x + y)

# Exercise 4
x = 5
y = 10
z = x + y
print(z)

# Exercise 5
x, y, z = "Orange", "Banana", "Cherry"

# Exercise 6
x = y = z = "Orange"

# Exercise 7
def myfunc():
    global x
    x = "fantastic"