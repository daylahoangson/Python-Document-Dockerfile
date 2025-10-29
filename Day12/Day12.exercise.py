# Bài tập 
# Level 1
# 1. Viết một hàm tạo ra một Random_user_id gồm sáu chữ số/ký tự.
import random 
import string 
def generate_random_user_id ():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id

# 2. Viết chương trình tạo số lượng user_id và ký tự do người dùng nhập. Ví dụ nhập 10 5 thì tạo 10 user_id có 5 ký tự.
def generate_multiple_user_id (num_ids, id_length):
    return [generate_random_user_id() for _ in range(num_ids)]
num_ids = int(input("Nhập số lượng user_id cần tạo: "))
id_length = int(input("Nhập độ dài mỗi user_id: "))
user_ids = generate_multiple_user_id(num_ids, id_length)
print("Danh sách user_id được tạo:")
for uid in user_ids:
    print(uid)

import random
import string

# Hàm tạo một user_id ngẫu nhiên với độ dài cho trước
def generate_random_user_id(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Hàm tạo nhiều user_id
def generate_multiple_user_id(num_ids, id_length):
    return [generate_random_user_id(id_length) for _ in range(num_ids)]

# Nhập từ người dùng
num_ids = int(input("Nhập số lượng user_id cần tạo: "))
id_length = int(input("Nhập độ dài mỗi user_id: "))

# Tạo danh sách user_id
user_ids = generate_multiple_user_id(num_ids, id_length)

# In kết quả
print("Danh sách user_id được tạo:")
for uid in user_ids:
    print(uid)

# 3. Viết hàm tạo ra các mã màu rgb (3 giá trị nằm trong khoảng từ 0 đến 255 mỗi giá trị). Ví dụ: rgb(125,244,255)
def generate_rgb_color ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"Mã màu là rgb({r},{g},{b})"

#Level 2
#1. Viết hàm list_of_hexa_colors trả về danh sách số lượng màu thập lục phân (16 ký hiệu, 0-9 và 6 chữ cái a-f).

def list_of_hexa_colors (num_colors):
    colors = []
    for _ in range (num_colors):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(color)
    return colors

# 2. Viết môt hàm list_of_rbg_color trả về danh sách số lượng màu RBG
def list_of_rbg_color (num_color):
    colors = []
    for _ in range (num_color):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append (f"rgb({r},{g},{b})")
    return colors
# 3. Gộp 2 hàm ở trên thành hàm generate_color có thể tạo ra bất cứ số lượng màu hexa rbg nào. 
def generate_color (type_color, num_color):
    if type_color == 'hexa':
        return list_of_hexa_colors (num_color)
    elif type_color == 'rbg':
        return list_of_rbg_color (num_color)
    else:
        return "Loại màu không hợp lệ. Vui lòng chọn 'hexa' hoặc 'rbg'."