def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
C = [i for i in range(3, 1001) if is_prime(i)]
M = [[C[i],C[i+1]] for i in range(len(C) - 1)]
print(M)