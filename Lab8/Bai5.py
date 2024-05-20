def sumPdivisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
def amicable(a, b):
    return a != b and sumPdivisors(a) == b and sumPdivisors(b) == a