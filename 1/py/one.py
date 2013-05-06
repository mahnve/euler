def sum_below(number):
    r = range(1, (number - 1))
    return sum(filter(multiple_of_3_or_5, r))

def multiple_of_3_or_5(candidate):
    return (candidate % 3 == 0) or (candidate % 5 == 0)


print(sum_below(1000))
