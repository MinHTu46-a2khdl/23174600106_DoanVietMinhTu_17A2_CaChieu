input_string = input("Nhập vào một chuỗi ký tự có độ dài hơn 10 ký tự: ")
print(f"""
Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8: {input_string[1:8]}
Chuỗi ký tự con gồm 5 ký tự từ vị trí thứ 5: {input_string[4:9]}
Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự: {input_string[-3:]}
Chuỗi sau khi chuyển đổi thành chữ thường: {input_string.lower()}
Chuỗi sau khi chuyển đổi thành chữ hoa: {input_string.upper()}
Chuỗi sau khi đảo ngược: {input_string[::-1]}
""")