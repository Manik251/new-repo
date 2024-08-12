def check_prime(n):
    if n <= 1:
        return "Composite"
    elif n <= 3:
        return "Prime"
    elif n % 2 == 0 or n % 3 == 0:
        return "Composite"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "Composite"
        i += 6
    return "Prime"

num = int(input("Enter a number: "))
print(check_prime(num))