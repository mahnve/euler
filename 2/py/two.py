def fibonacci(n):
    sum = 0
    first = 0
    second = 1
    current = 0
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = 0
sum = 0
while(fibonacci(n) <= 4000000):
    fib = fibonacci(n)
    if(fib%2 == 0):
        sum = sum + fib
    n = n + 1

print(sum)
