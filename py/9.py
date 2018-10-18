from math import sqrt, floor


def is_pythagorean_triplet(a, b, c):
    return (a * a + b * b) == (c * c)


def find_pythagorean_triplet_with(sum):
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, int(sqrt(a * a + b * b)) + 1):
                if a == 2 and b == 3 and c == 5:
                    print"{0} {1} {2}".format(a, b, c)
                if is_pythagorean_triplet(a, b, c):
                    print("a:{0} b:{1} c:{2} is a triplet".format(a, b, c))
                    if a + b + c == 1000:
                        print ("And the sum is 1000!")
                        return [a, b, c]


print(find_pythagorean_triplet_with(1000))


def test_identifies_pythagorean_triplet():
    assert is_pythagorean_triplet(3, 4, 5)


def test_refutes_non_pythagorean_triplet():
    assert not is_pythagorean_triplet(2, 5, 8)

