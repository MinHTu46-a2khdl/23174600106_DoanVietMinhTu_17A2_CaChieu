kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = {san_pham: (so_luong, gia_tien[san_pham], so_luong * gia_tien[san_pham]) 
           for san_pham, so_luong in kho.items()}
# In hóa đơn
print("Hóa đơn mua hàng:")
for san_pham, (so_luong, don_gia, thanh_tien) in hoa_don.items():
    print(f"{san_pham},Số lượng: {so_luong}, Đơn giá: {don_gia},Số tiền: {thanh_tien}")

print(f"Tổng số tiền của hóa đơn: {sum(kho[san_pham] * gia_tien[san_pham] for san_pham in kho)}")
print("\nSố lượng của các mặt hàng trong kho sau khi mua:")
for san_pham, so_luong in kho.items():
    print(f"{san_pham}: {so_luong}")
                  