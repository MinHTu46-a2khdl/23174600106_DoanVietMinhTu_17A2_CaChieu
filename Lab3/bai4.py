#bai4
#a
print("\n".join([" " * (5 - i) + "* " *( i+1) if i < 5 else " " * (i-4) + "* " * (10-i)   for i in range(10)]))
#b
print("\n".join([" " * (7 - i) + "*" *( 2*i-1) if i < 7 else " " * 5 + "***" for i in range(10)]))