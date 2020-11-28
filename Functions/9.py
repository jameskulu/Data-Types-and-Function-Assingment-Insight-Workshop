# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.


def check_prime_number(num):
    if num == 1:
        print('It is not a prime number\n')
    for i in range(2, num):
        if (num % i) == 0:
            print("it is not a prime number\n")
            break
    else:
        print('It is a prime number\n')


check_prime_number(2)
