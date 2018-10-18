PRIME_TO_FIND = 10001

def prime_no(no):
    current_prime = 0
    to_test = 1
    while(current_prime < no):
        to_test += 1
        if(is_prime(to_test)):
            current_prime += 1
    return to_test

def is_prime(number):
    for x in range(2, number):
        if(number%x == 0):
            return False
    return True

print(prime_no(PRIME_TO_FIND))
