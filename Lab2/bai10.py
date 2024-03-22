#bai10
def check_available(category, time_slot):
  """
  Hàm kiểm tra xem thời gian chiếu phim có phù hợp với thể loại phim hay không.

  Tham số:
    category: Thể loại phim.
    time_slot: Khung giờ chiếu phim.

  Trả về:
    True nếu thời gian chiếu phim phù hợp với thể loại phim, False nếu không.
  """

  if category == "Tình cảm" or category == "Kinh dị":
    return time_slot in "Tối"
  elif category == "Hoạt hình":
    return time_slot in ["Trưa", "Chiều"]
  else:
    return True

def main():
  """
  Hàm chính của chương trình.
  """
  # Danh sách thể loại phim
  categories = ["Hành động", "Kinh dị", "Tình cảm", "Hoạt hình", "Hài hước"]

  # Danh sách khung giờ chiếu phim
  time_slots = ["Sáng", "Trưa", "Chiều", "Tối"]

  # Lặp lại chương trình cho đến khi người dùng thoát
  while True:
    # Hiển thị logo rạp phim
    print("Beta Cinema")

    # Chào mừng khách hàng
    print("Kính chào quý khách đến với rạp chiếu phim Beta Cinema!")

    # Giới thiệu về rạp phim
    print("Beta Cinema tự hào sở hữu kho phim hơn 10.000 bộ phim thuộc mọi thể loại, từ hành động, kinh dị, tình cảm đến hài hước, hoạt hình. Chúng tôi phục vụ quý khách tất cả các ngày trong tuần, từ sáng đến tối.")

    # Lựa chọn thể loại phim
    print("\nQuý khách vui lòng lựa chọn thể loại phim:")
    for i, category in enumerate(categories):
      print(f"({i + 1}) {category}")

    # Lựa chọn khung giờ chiếu phim
    print("\nQuý khách vui lòng lựa chọn thời gian chiếu phim:")
    for i, time_slot in enumerate(time_slots):
      print(f"({i + 1}) {time_slot}")

    # Xác nhận lựa chọn
    choice_category = int(input("\nLựa chọn thể loại phim: "))
    choice_time_slot = int(input("Lựa chọn khung giờ chiếu phim: "))

    category = categories[choice_category - 1]
    time_slot = time_slots[choice_time_slot - 1]

    # Kiểm tra tính hợp lệ của lựa chọn
    if not check_available(category, time_slot):
      print(f"\nKhông có suất chiếu phim {category} vào buổi {time_slot}.")
      continue

    print(f"\nQuý khách đã lựa chọn phim thuộc thể loại {category}, chiếu vào buổi {time_slot}. Xin cảm ơn quý khách.")

    # Hỏi người dùng muốn tiếp tục hay thoát
    choice = input("Quý khách muốn tiếp tục lựa chọn phim khác hay tiến hành thanh toán? (c/t): ")

    # Thoát chương trình nếu người dùng nhập 't'
    if choice.lower() == "t":
      break
if _name_ == "_main_":
  main()