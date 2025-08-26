#Level 1
# 1. Khai báo biến
first_name = 'Arnold'
last_name = 'Pham'
full_name = 'Arnold Pham'
country = 'VietNam'
city = 'Ha Noi'
age = 100
year = 2025
is_maried = False
skills = ['C', 'Python']

#Level 2
# 1. Kiểm tra kiểu dữ liệu của các biến đã khai báo
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_maried))
print(type(skills))

# 2. Tìm độ dài của tên của bạn
print(len(first_name))

# 3. Thực hiện các phép toán số học
num_one = 5
num_two = 4
a = num_one + num_two
b = num_one * num_two
c = num_one - num_two
d = num_one / num_two
e = num_one % num_two
f = num_one ** num_two
g = num_one // num_two

print ('Kết quả:', [a, b, c, d, e, f, g])

# 4.
C = 30 #bán kính
# diện tích hình tròn
pi = 3.14
area_of_circle = pi * C** 2
print('Diện tích hình tròn là: ', area_of_circle)
# chu vi hình tròn
circumference_of_circle = 2 * pi * C
print('Chu vi hình tròn là: ', circumference_of_circle)
# lấy giá trị bán kính và tính diện tích, chu vi hình tròn
N = int(input('Nhập bán kính hình tròn: '))
area_of_circle = pi * N** 2
print('Diện tích hình tròn là: ', area_of_circle)
circumference_of_circle = 2 * pi * N
print('Chu vi hình tròn là: ', circumference_of_circle)
# 5. Sử dụng hàm input() để lấy tên, họ, quốc gia và tuổi từ người dùng và lưu giá trị vào tên biến tương ứng
first_name = input('Nhập tên: ')
last_name = input('Nhập họ: ')
country = input('Nhập quốc gia: ')
age = int(input('Nhập tuổi: '))

print('Thông tin cá nhân:', last_name, '/', first_name,'/', age, '/', country)
