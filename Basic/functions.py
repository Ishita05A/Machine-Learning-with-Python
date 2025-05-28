def greet(First_name, Last_name):
    print("Hello ", f"{First_name} {Last_name}")
    print("Welcome Abroad")


def increment(number, by=1):
    return number+by


def multiply(*num):
    total = 1
    for i in num:
        total *= i
    return total


greet("Ishita", "Agarwal")
greet("Harshita", "Pandey")

print(increment(5, 2))

print(multiply(3, 4, 5, 2, 1))
