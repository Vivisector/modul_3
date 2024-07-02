print('\n##### Простые числа #####')
# isPrime = False
'''
primes = []
for num in range(2, 99):
    isPrime = True
    for j in range(2, num // 2 + 1):
        if num % j == 0:
            isPrime = False
            break
        else:
            isPrime = True
    if isPrime == True: primes.append(num)
'''

is_prime = lambda num: all(num % j != 0 for j in range(2, int(num ** 0.5) + 1))
primes = [num for num in range(2, 99) if is_prime(num)]
print(*primes)
