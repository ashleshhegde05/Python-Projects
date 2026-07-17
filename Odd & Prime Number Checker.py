# Even/Odd and Prime Number Checker

def check_even_odd(num):
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

def check_prime(num):
    if num <= 1:
        print("It is not a Prime Number.")
        return

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("It is not a Prime Number.")
            return

    print("It is a Prime Number.")

number = int(input("Enter a number: "))

check_even_odd(number)
check_prime(number)