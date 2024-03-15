#bài four
canh_day = float(input("Nhập độ dài cạnh đáy: "))
chieu_cao = float(input("Nhập chiều cao: "))
  
dien_tich_xq = 2* canh_day * chieu_cao
dien_tich_tp = dien_tich_xq +canh_day ** 2
the_tich = (1 / 3)* (canh_day * 2)* chieu_cao
print(f"Diện tích xung quanh: {dien_tich_xq:.2f}")
print(f"Diện tích toàn phần: {dien_tich_tp:.2f}")
print(f"Thể tích: {the_tich:.2f}")