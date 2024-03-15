# bài 9
# Nhập tọa độ các điểm M, N, P, Q
mx, my = map(float, input("Nhập tọa độ x, y của điểm M: ").split())
nx, ny = map(float, input("Nhập tọa độ x, y của điểm N: ").split())
px, py = map(float, input("Nhập tọa độ x, y của điểm P: ").split())
qx, qy = map(float, input("Nhập tọa độ x, y của điểm Q: ").split())

# Tính tọa độ trung điểm của mỗi cạnh
# Trung điểm MN
mnx = (mx + nx) / 2
mny = (my + ny) / 2

# Trung điểm NP
npx = (nx + px) / 2
npy = (ny + py) / 2

# Trung điểm PQ
pqx = (px + qx) / 2
pqy = (py + qy) / 2

# Trung điểm QM
qmx = (qx + mx) / 2
qmy = (qy + my) / 2

# In ra kết quả
print("Tọa độ trung điểm MN:", mnx, mny)
print("Tọa độ trung điểm NP:", npx, npy)
print("Tọa độ trung điểm PQ:", pqx, pqy)
print("Tọa độ trung điểm QM:", qmx, qmy)