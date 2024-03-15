# bài three
so_tien_ban_dau = float(input("Nhập số tiền ban đầu: "))
lai_suat_hang_nam = float(input("Nhập lãi suất hàng năm: "))
amoun_after_5_years = so_tien_ban_dau * (1 + lai_suat_hang_nam / 100) ** 5
amoun_after_10_years = so_tien_ban_dau * (1 + lai_suat_hang_nam / 100) ** 10
grow_rate = (amoun_after_10_years-amoun_after_5_years)*100/amoun_after_5_years
print(f"Số tiền sau 5 nam là: {amoun_after_5_years:.2f}")
print(f"Số tiền sau 10 nam là: {amoun_after_10_years:.2f}")
print(f"Tỷ lệ tăng trưởng là: {grow_rate:.2f}%")