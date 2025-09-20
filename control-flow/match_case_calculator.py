<<<<<<< HEAD
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation  = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
        print("The result is : ",  result)
    case "-":
        result = num1 - num2
        print("The result is : ",  result)
    case "*":
        result = num1 * num2
        print("The result is : ",  result)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = (num1 / num2)
            print("The result is : ",  result)
    case _:
        print("Invalid operation.")

=======
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation  = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
        print("The result is : ",  result)
    case "-":
        result = num1 - num2
        print("The result is : ",  result)
    case "*":
        result = num1 * num2
        print("The result is : ",  result)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = (num1 / num2)
            print("The result is : ",  result)
    case _:
        print("Invalid operation.")

>>>>>>> a2ff1d0c1d2be792f8ce72a34bbfcb8058a7ef58
