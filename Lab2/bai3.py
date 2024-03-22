#bai3
def read_number(number):
  # Danh sách các số từ 1 đến 9
  ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

  # Danh sách các số từ 10 đến 19
  teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

  # Danh sách các số chục
  tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
  hundreds = number // 100
  tenss = (number % 100) // 10
  oness = number % 10
  a = ones[hundreds - 1] + " hundred " 
  if tenss == 0:
    return  a if oness == 0 else a + ones[oness - 1]
  elif tenss == 1:
    return a + teens[(number % 100)-10]
  else :
      return a + tens[tenss -2] if oness == 0 else a + tens[tenss -2]+ " " + ones[oness - 1]

number = int(input("Nhập số nguyên dương có 3 chữ số: "))
print(f"Số {number} được đọc là: {read_number(number)}")
