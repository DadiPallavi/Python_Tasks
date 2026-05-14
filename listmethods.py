#1. What happens to the length of a list after calling the append() method?
#The length of the list increases by 1.

#2. Where is the new element placed when you use list.append(x)?
#The new element is added at the end of the list.

#3. Write a simple line of code to add the string 'apple' to a list named fruits.
#fruits.append('apple')

#4. If you append a list [10, 20] to an existing list [1, 2], what is the total number of elements in the final list?
#my_list = [1, 2]
#my_list.append([10, 20])
#print(my_list)


#5. Explain the difference in result between list.append([5, 6]) and list + [5, 6].
#append([5, 6])
#Adds the entire list as one element.
#a = [1, 2]
#a.append([5, 6])
#print(a)
#[1, 2, [5, 6]]
#list + [5, 6]
#Adds elements individually and creates a new list.
#a = [1, 2]
#b = a + [5, 6]
#print(b)

#1. Does the extend() method add elements individually or as a single nested object?
#extend() adds elements individually.

#2. What type of argument does the extend() method expect?
#It expects an iterable (like a list, tuple, string, set, etc.).

#3. How do you merge list B into list A using extend()?
#A.extend(B)

#4.my_list = [1, 2]
#my_list.extend('34')
#print(my_list)
#Output:--[1, 2, '3', '4']

#5. What is the difference between extend() and the += operator for lists, if any?
#extend() is a list method.
#+= is an operator.

#1. How many arguments does the insert() method take?
#It takes 2 arguments:
#Index position
#Element to insert

#2. If you want to add an element at the very beginning of a list, what index should you use in insert()?
#Use index 0.

#3. Does insert() replace the existing element at the given index or shift it?
#It shifts the existing elements to the right.

#4. What happens if you use a negative index, like list.insert(-1, 'x'), on a list of 3 items?
a = [1, 2, 3]
a.insert(-1, 'x')
print(a)

#5. In terms of performance, why is insert(0, x) considered slower than append(x) for large lists?
#append(x) adds the item at the end, so it is very fast.
#insert(0, x) adds at the beginning, so all existing elements must shift one position to the right.
