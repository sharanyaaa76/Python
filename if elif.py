age = int(input("Enter your age: "))

if age <= 12:
    print("You are a kid!")
elif age <= 17:
    print("You are a teenager.")
elif age == 18:
    print("You are 18 and in adulthood.")
else:
    print("You are above 18.")