number = int(input("Enter the size of the pattern:"))

counter = 1

while counter == 1:
    print (f"*" * number)
    counter+=1
    for counter in range(2 , number):
        print(f"*" * number)