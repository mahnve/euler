candidate = 1

def evenly_dividable(candidate):
    for divisor in range(1,21):
        if(candidate % divisor != 0):
            if(divisor > 15):
                print("{0} failed at {1}".format(candidate, divisor))
            return False
    return True


while not evenly_dividable(candidate):
    candidate += 1
    if(candidate % 1000000 == 0):
        print("Current: {}".format(candidate))
print("Answer: {}".format(candidate))
