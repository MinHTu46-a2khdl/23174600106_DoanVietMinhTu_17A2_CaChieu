#1)
def cubesum(n):
    return sum([int(digit)**3 for digit in str(n)])
#2a)
def PrintArmstrong(n):
    for i in range(n):
        if cubesum(i) == i:
            print(i, end=" ")
#2b)
def isArmstrong(n):
   return cubesum(n) == n