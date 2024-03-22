#bai9
a,b = float(input("nhap he so goc:")),float(input("nhập hệ số tự do:"))
f = abs(a*float(input("nhập hoang do tam duong tron:"))+b*float(input("nhập tung do tam duong tron:")) - 1)/(a**2+b**2)**0.5
R = float(input(" nhập ban kinh  đường tròn :"))
print(" duong tron tiep xuc duong thang" if f == R else " duong tron cat duong thang" if f < R else " duong tron nam ngoai duong thang" )

