tong = so_luong_so = 0
chuoi_so = chuoi_so_le = chuoi_so_chan =   ""

while tong <= 1000:
        so = int(input("Nhập số: "))
        tong += so
        so_luong_so += 1
        chuoi_so += f"{so} "  
        if so % 2 != 0:
            chuoi_so_le += f"{so} "
        else:
            chuoi_so_chan += f"{so} "
print(f"Các số đã nhập: {chuoi_so.strip()}")            
print(f"a) Các số lẻ đã nhập: {chuoi_so_le.strip()}")
print(f"b) Các số chẵn đã nhập: {chuoi_so_chan.strip()}")
print(f"c) Số lượng số đã nhập: {so_luong_so}")