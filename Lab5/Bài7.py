c = input()
print(f"""
Số chữ hoa: {sum(1 for r in c if r.isupper())}
Số chữ thường: {sum(1 for r in c if r.islower())}
Số chữ số: {sum(1 for r in c if r.isdigit())}
Số ký tự đặc biệt: {sum(1 for r in c if not r.isalnum())}
""")