#Example
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Example
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Example
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Example
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Example
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Example
set1 = {"abc", 34, True, 40, "male"}

#Example
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Example
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Example
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Example
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Example
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#Example
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Example
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#Example
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

