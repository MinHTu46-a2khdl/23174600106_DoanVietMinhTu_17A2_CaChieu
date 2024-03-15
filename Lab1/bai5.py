#bai five
toa_do_a = tuple(map(float, input("Nhập tọa độ vectơ A (x, y): ").split()))
toa_do_b = tuple(map(float, input("Nhập tọa độ vectơ B (x, y): ").split()))
do_dai_a = (toa_do_a[0]**2 + toa_do_a[1]**2)**0.5
do_dai_b = (toa_do_b[0]**2 + toa_do_b[1]**2)**0.5
 
print("Tọa độ vectơ A + B: ",toa_do_a[0] + toa_do_b[0], toa_do_a[1] + toa_do_b[1])
print("Tọa độ vectơ A - B: ",toa_do_a[0] - toa_do_b[0], toa_do_a[1] - toa_do_b[1])
print(f"Độ dài vectơ A: {do_dai_a:.2f}")
print(f"Độ dài vectơ B: {do_dai_b:.2f}")
print(f"Cosin góc giữa hai vectơ A và B: {(toa_do_a[0] * toa_do_b[0] + toa_do_a[1] * toa_do_b[1]) / (do_dai_a * do_dai_b):.2f}")