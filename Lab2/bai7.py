#bai7
c = float(input(" can nang la(kg) "))/(float(input("chieu cao la(met) "))**2)
print(" chi so BMI la", "beo" if c >= 30 else " hoi beo " if c >= 25 else " binh thong" if c >= 18.5 else " gay")