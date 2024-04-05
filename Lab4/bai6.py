b = ""
for i in str(input("nhap so nguyen ")):
      so = int(i)
      if so == 0:
           ket_qua = "zero"
      elif so == 1:
           ket_qua = "one"
      elif so == 2:
           ket_qua = "two"
      elif so == 3:
           ket_qua = "three"
      elif so == 4:
           ket_qua = "four"
      elif so == 5:
           ket_qua = "five"
      elif so == 6:
           ket_qua = "six"
      elif so == 7:
           ket_qua = "seven"
      elif so == 8:
           ket_qua = "eight"
      else :
           ket_qua = "nine"
      b += " " + ket_qua
print(b)     