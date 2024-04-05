while True:
  so_1,so_2 = float(input("nhập số ")),float(input("nhập số "))  
  print(f"{so_1} + {so_2} = {so_1 + so_2}")
  print(f"{so_1} - {so_2} = {so_1 - so_2}")
  print(f"{so_1} * {so_2} = {so_1 * so_2}")
  print(f"{so_1} / {so_2} = {so_1 / so_2}")
  print(f"{so_1} ^ 2 = {so_1 ** 2}")
  print(f"{so_2} ^ 2 = {so_2 ** 2}")
  tiep_tuc = input("Bạn có muốn tiếp tục chương trình? (yes/no): ")
  if tiep_tuc.lower() != "yes":
    break
#6