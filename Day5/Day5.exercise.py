## Bài tập 
## Level 1

# 1. Khai báo list có tên it_companies và gán các giá trị ban đầu Facebook, Google, Microsoft, Apple, IBM, Oracle và Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 2. In danh sách các công ty
print (it_companies)

# 3. In công ty đàu tiên, công ty ở giữa và công ty cuối cùng
frist_lenght = len(it_companies)
middle_lenght = frist_lenght // 2
last_lenght = frist_lenght - 1
print (it_companies[0], it_companies[middle_lenght], it_companies[last_lenght])

# 4. in danh sách sau khi sửa đổi một trong các công ty

it_companies[0] = 'Meta'
print (it_companies)

# 5. Thêm một công ty CNTT vào it_companies
it_companies.append('EPIC')
print (it_companies)

# 6. Chèn một công ty CNTT vào giữa danh sách it_companies
it_companies.insert(middle_lenght, 'EMIR ')
print (it_companies)

# 7. Nối it_companies với chuỗi '#;'
it_companies_str = '#;'.join(it_companies)
print (it_companies_str)

# Kiểm tra xem môt công ty nào đó có tồn tại trong list it_companies hay không
check_company = 'Meta' in it_companies
print (check_company)

# 9. Sắp xếp list bằng phương thức sort()

it_companies.sort()
print (it_companies)
it_companies.sort(reverse=True)
print (it_companies)
 
# 10. Đảo ngược list theo thứ tự giảm dần bằng hàm revevse()
it_companies.reverse()
print (it_companies)

# 11 Xóa 3 phần tử đầu tiên của lits 

it_companies.pop(0)
it_companies.pop(0)
it_companies.pop(0)
print (it_companies)

# 12. Xóa toàn bộ lits
it_companies.clear()
print (it_companies)


## Level 2

# Danh sách tuổi 10 học sinh : age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2. sắp xếp danh sách và tìm tuổi nhỏ nhất và lớn nhắt 
age.sort()
print (age)
min_age = age[0]
max_age = age[-1]
print (min_age, max_age)

# 3. Thêm lại tuổi nhỏ nhất và lớn nhất vào danh sách
age.append(min_age)
age.append(max_age)

# 4. Tìm độ tuổi trung bình (phần tử ở giữu hoặc hai phần tử ở giữa chia đôi)
age.sort()
print (age)
length_age = len(age)
if length_age % 2 == 0:
    middle1 = age[length_age // 2]
    middle2 = age[length_age // 2 - 1]
    median = (middle1 + middle2) / 2
else:
    median = age[length_age // 2]
print (median)  

# 5. Tìm độ tuổi trung bình (tổng tất cả các phần tử chia cho độ dài lits)
total_age = sum(age)
averge_age = total_age / length_age
print (averge_age)

# 6. Tìm phạm vi tuổi (tuổi lớn nhất - tuổi nhỏ nhất)
age_range = max_age - min_age
print (age_range)

# 7. So sánh giá trị của ( tối thiểu - trung bình ) và ( tối đa - trung bình ), sử dụng hàm abs()
min_diff = abs(min_age - averge_age)
max_diff = abs(max_age - averge_age)
print (min_diff, max_diff)

# 8. Sắp xếp danh sách và unpaking các phần tử vào các biến nhoHon23, lonHon23
age.sort()
print (age)
nhoHon23 = []
lonHon23 = []
for a in age:
    if a < 23:
        nhoHon23.append(a)
    else:
        lonHon23.append(a)
print (nhoHon23)
print (lonHon23)
print (len(nhoHon23), len(lonHon23))

