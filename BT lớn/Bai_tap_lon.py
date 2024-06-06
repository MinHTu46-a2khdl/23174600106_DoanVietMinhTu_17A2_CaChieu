import random
import csv

def rut_so():
    return random.randint(1, 100)

def kiem_tra_ket_qua(so_du_doan, so_rut):
    return so_du_doan == so_rut

def tinh_xac_suat_trung_giai(so_du_doan, so_rut):
    return "100%" if kiem_tra_ket_qua(so_du_doan, so_rut) else '0%'

def main():
    so_lan_choi = int(input("Nhập số lần chơi(tối đa 5 lần): "))
    while so_lan_choi > 5:
        print("số lần chơi của bạn đã vượt quá 5 . Vui lòng nhập lại")
        so_lan_choi = int(input("Nhập số lần chơi(tối đa 5 lần): "))
    so_du_doan = set()
    
    so_rut_list = []
    for _ in range(so_lan_choi):
        so_du_doan_input = int(input("Nhập số dự đoán (từ 1 đến 100): "))
        if len(so_du_doan) < so_lan_choi:
            so_du_doan.add(so_du_doan_input)
    
    for _ in range(so_lan_choi):
        so_rut = rut_so()
        so_rut_list.append(so_rut)
    
    with open('ket_qua.csv', 'w', newline='') as csvfile:
        fieldnames = ['So_du_doan', 'So_rut', 'Xac_suat_trung_giai']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, so_du_doan_item in enumerate(so_du_doan):
            if i < len(so_rut_list):  
                writer.writerow({'So_du_doan': so_du_doan_item, 'So_rut': so_rut_list[i], 'Xac_suat_trung_giai': tinh_xac_suat_trung_giai(so_du_doan_item, so_rut_list[i])})
    
    print("\nKết quả:")
    for i, so_du_doan_item in enumerate(so_du_doan):
        if i < len(so_rut_list): 
            a = tinh_xac_suat_trung_giai(so_du_doan_item, so_rut_list[i])
            print(f"Số dự đoán: {so_du_doan_item}, Số rút: {so_rut_list[i]}, Xác suất trúng giải: {a}")
            if a == "100%":
                print("bạn đã đoán đúng, chúc mừng bạn nhận được 1 triệu")

if __name__ == "__main__":
    main()