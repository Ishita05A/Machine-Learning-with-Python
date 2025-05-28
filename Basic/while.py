num = 100
while num > 0:
    print(num)
    num //= 2

print()

command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)
