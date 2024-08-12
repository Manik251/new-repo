a=input("Enter First number: ")
b=input("Enter Second number: ")
c=input("Enter Third number: ")
if a>b and a>c:
    # print("a", a,"is greater than",b,"and",c)
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
else:
     print(f"{c} is greater than {a} and {b}")
  
