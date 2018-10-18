numbers = range(1,101)
numbers_squared_individually = [x*x for x in numbers]

sum_numbers = sum(numbers)
sum_numbers_squared = sum_numbers * sum_numbers
sum_numbers_squared_individually = sum(numbers_squared_individually)
answer = sum_numbers_squared - sum_numbers_squared_individually

print("Answer: {}".format(answer))
