def is_armstrong(n):
    num = n
    nod = len(str(n))
    total = 0

    while num > 0:
        last_digit = num % 10
        total += last_digit ** nod
        num //= 10

    return total == n

print(is_armstrong(153))
print(is_armstrong(123))