1. creating a list

fruits = ["cherry","blueberry","banana","kiwi","orange"]
print(fruits)

2.Accessing Elements

colors = ['red','blue','green','yellow','purple']
print("first element:",colors[0])
print("third element:",colors[2])
print("last element:",colors[-1])

3.Modifying List

numbers = [10,20,30,40,50,]
numbers[1] = "25"
numbers[4] = "60"
print(numbers)

4.List Slicing

names = ["Alice","Bob","Charlie","David","Emma"]
subset = names[:3]
print(subset)

5.Looping through a List

numbers = list(range(1,11))
for i in numbers:
 print(i**2)

6.List Methods:Append and Extend

shopping_cart = []
shopping_cart1 = ['butter','cheese']
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
shopping_cart.extend(shopping_cart1)
print(shopping_cart)

7.Finding Maximum and Minimum in a list

numbers = [45,22,88,56,92,33]
print("Maximum number:",max(numbers))
print("Minimum number:",min(numbers))

8.Counting Occurrences

letters = ['a','b','a','c','b','a','d']
count_of_a = letters.count('a')
print("count of a:",count_of_a)

9.List Comprehension

even_number = [i**2 for i in range(0,11,2)]
print(even_number)

10.Removing Duplicates

nums =[1,2,2,3,4,4,5,6,6,7]
num_set= set([1,2,2,3,4,4,5,6,6,7])
print(num_set)