number = int(input("Enter the size of the pattern:"))

row = 1

while row == 1:
    for col in range(number):
        print("*", end="")
    print()
    row+=1
for row in range(2, number+1):
    for col in range(number):
        print("*", end="")
    print()