
#bai3
print(3)
#a
print("a)",sum(i for i in range(100, 1001) if all(i % d != 0 for d in range(2, int(i**0.5) + 1))))
#b
print("b)",*[ i**2 for i in range(1,round(1001**0.5))])
#c
def fib_sequence():
    a, b = 0, 1
    while a < 100:
        yield a
        a, b = b, a + b
print("c)",", ".join([str(fib) for fib in fib_sequence()]))
#d
print("d)",*[i for i in range(1,500) if sum(v for v in range(1,i) if i % v == 0 ) == i])
#e
print("e)", sum(i * (3 * i - 1) / 2 for i in range(1, 200) if i * (3 * i - 1) / 2 <= 200))
