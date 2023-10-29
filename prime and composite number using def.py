#prime and composite number using function.
def is_prime(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    print(primes)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
is_prime(start, end)