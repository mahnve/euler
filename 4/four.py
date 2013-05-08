RANGE1 = 10000
RANGE2 = 10000

def find_highest_palindrome_product():
    return max(find_palindromes_in_range(RANGE1, RANGE2))

def find_palindromes_in_range(range1, range2):
    return [x*y
            for x in range(1,range1)
            for y in range(1,range2)
            if(is_palindrome_number(x*y))]

def is_palindrome_number(product):
    product_as_string = str(product)
    reversed_product = product_as_string[::-1]
    return product_as_string == reversed_product

print("Largest palindrome is {}".format(find_highest_palindrome_product()))
