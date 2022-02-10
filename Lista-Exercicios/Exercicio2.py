def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input('insira um valor: '))

for i in range(1,n+1):
    x = int(fibonacci(i))
    if x == n:
        print('\nO valor inserido pertence a sequencia!')
    else:
        print('\nO valor inserido não pertence a sequencia!')