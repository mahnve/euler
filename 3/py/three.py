from math import floor

NUMBER=600851475143

def dividable(divisor):
    return (NUMBER%divisor == 0)

def prime(number):
    for x in range(2,number):
        if(number%x == 0):
            return False
        else:
            continue
    return True

def find_highest_prime():
    for x in range(3, floor(NUMBER/2)):
        if(dividable(x)):
            candidate = (NUMBER//x)
            print("Candidate: {}".format(candidate))
            if(prime(candidate)):
                return candidate
            else:
                print("... not prime though")
                continue

print("{} is the highest prime".format(find_highest_prime()))
