fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

for fruit in fruits:
    print(fruit)

print('====================\n')

# access list with index
print(fruits[0]) # apple
print(fruits[-2]) # cherry
print(fruits[1:5]) # ['banana', 'cherry', 'orange', 'kiwi']

# list method
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(10) # add 10 to the end of the list
print(numbers)
print('====================\n')

numbers.insert(2,7) # add 7 to index 2
print(numbers)
print('====================\n')

numbers.remove(7) # remove number 3 from the list (remove value)
print(numbers)
print('====================\n')

numbers.pop() # remove the last element from the list
print(numbers)

numbers.pop(2) # remove element with index 2
print(numbers)