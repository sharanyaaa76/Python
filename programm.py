# Program to create an array using user input

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Array elements are:", arr)