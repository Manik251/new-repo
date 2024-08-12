a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
operator=(input("Enter the operations you want to perform: "))
if operator == "+":
    sum=(a+b)
    print("The addition of two number is: ",sum)
elif operator == "-":
    difference=(a-b)
    print("The difference of two number is: ", difference)
elif operator == "*":

    product=(a*b)
    print("The product of two number is: ", product)
elif operator == "/":
    if b == 0:
        print("Error! Division by zero is not allowed.")
    else:
        quotient=(a/b)
        print("The quotient of two number is: ", quotient)
else:
    print("Invalid operator")