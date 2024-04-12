danh_sach = input("Nhập vào một chuỗi văn bản: ").split()
w = input("Nhập vào một từ để tìm vị trí: ")
if w in danh_sach:
    print(f"Vị trí của từ '{w}' trong chuỗi là: {danh_sach.index(w)}")
else:
    print(f"Từ '{w}' không có trong chuỗi.")
max_count = max(danh_sach.count(i) for i in danh_sach)
for i in danh_sach:  
    if max_count == danh_sach.count(i):
        print(f"Từ xuất hiện nhiều nhất là: '{i}' với {max_count} lần.")
        break