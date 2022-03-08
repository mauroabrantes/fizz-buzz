### Desafio FizzBuzz ###

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 ==0:
        return f'fizzbuzz, {n} parou no divisivel por 3 e 5'
    if n % 3 == 0:
        return f'fizz, {n} parou no divisivel por 3'
    if n % 5 == 0:
        return f'buzz, {n} parou no divisivel por 5'
    return n

from random import randint

for i in range(10):
    aleatorio = randint(0, 30)
    print(fizz_buzz(aleatorio))