# Nhập Ma trận
def nhap_ma_tran():
    m, n = map(int, input("Nhập kích thước ma trận m x n (m n): ").split())
    return [list(map(int, input(f"Nhập {n} số vào hàng {i+1}: ").split())) for i in range(m)]

# Tổng của Ma trận
def tong_ma_tran(mt):
    return sum(sum(row) for row in mt)

# Tích của Ma trận
def tich_ma_tran(mt1, mt2):
    if len(mt1[0]) != len(mt2):
        return None
    result = [[0 for _ in range(len(mt2[0]))] for _ in range(len(mt1))]
    for i in range(len(mt1)):
        for j in range(len(mt2[0])):
            for k in range(len(mt2)):
                result[i][j] += mt1[i][k] * mt2[k][j]
    return result
# Ma trận chuyển vị
def ma_tran_chuyen_vi(mt):
    mt_chuyen_vi = []
    for i in range(len(mt[0])):
        hang_moi = []
        for row in mt:
            hang_moi.append(row[i])
        mt_chuyen_vi.append(hang_moi)
    return mt_chuyen_vi
#bai6.2    
def nhap_ma_tran_vuong():
    n = int(input("Nhập kích thước ma trận vuông n x n (n): "))
    return [list(map(int, input(f"Nhập {n} số vào hàng {i+1}: ").split())) for i in range(n)]    
def kiem_tra_ma_tran_doi_xung(mt):
    return mt == ma_tran_chuyen_vi(mt)
if __name__ == "__main__":
#6.1    
    mt1 = nhap_ma_tran()
    print("Tổng của ma trận:", tong_ma_tran(mt1))
    
    mt2 = nhap_ma_tran()
    if len(mt1[0]) == len(mt2):
        tich = tich_ma_tran(mt1, mt2)
        if tich is not None:
            print("Tích của hai ma trận:\n", tich)
        else:
            print("Không thể tính tích của hai ma trận với kích thước không phù hợp.")
    else:
        print("Không thể tính tích vì số cột của ma trận thứ nhất không bằng số hàng của ma trận thứ hai.")
    
    print("Ma trận chuyển vị của ma trận thứ nhất:\n", ma_tran_chuyen_vi(mt1))
#b.2    
    mt_vuong = nhap_ma_tran_vuong()
    if kiem_tra_ma_tran_doi_xung(mt_vuong):
        print("Ma trận là ma trận đối xứng.")
    else:
        print("Ma trận không phải là ma trận đối xứng.")
        
