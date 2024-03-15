# bài two
def quan_ly_thu_vien(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong):
  thong_tin_sach = f"""
Thư viện ĐHKTKTCN có {so_luong} sách {ten_sach} với mã số {ma_sach}. Cuốn sách của tác giả {tac_gia} được xuất bản vào năm {nam_xuat_ban}.
  """
  return thong_tin_sach
ma_sach = input("Nhập mã sách: ")
ten_sach = input("Nhập tên sách: ")
tac_gia = input("Nhập tác giả: ")
nam_xuat_ban = int(input("Nhập năm xuất bản: "))
so_luong = int(input("Nhập số lượng sách: "))
thong_tin_sach = quan_ly_thu_vien(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong)
print(thong_tin_sach)
