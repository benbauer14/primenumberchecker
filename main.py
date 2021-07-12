def primeNumberChecker(number):
    for prime in range(2,number -1):
        if(number % prime == 0):
            return "not a prime number"
            break
    return "prime number"

print(primeNumberChecker(83))