def sumPdivisors(n):
    return sum(i for i in range(1, n) if n % i == 0)