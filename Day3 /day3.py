print(3 > 2 and 4 > 3) # True 
print(3 > 2 and 4 < 3) # False 
print(3 < 2 and 4 < 3 ) # False
print('True and True', True and True) # True
print(3 >= 2 or 4 >= 3) # True
print(3 >= 2 or 4 < 3) # Trüe
print(3 < 2 or 4 < 3) # False
print( 'True or False:', True or False) #True
print(not 3 > 2) # False
print(not True) #False
print(not False) # True
print(not not True) # True
print(not not False) # False


# 1. Khai báo tuổi dưới dạng số nguyên (int)
tuoi = 23

# 2. Khai báo chiều cao dưới dạng số thực (float)
chieu_cao = 1.75

# 3. Khai báo số phức (complex)
so_phuc = 3 + 4j

# Nhập đáy và chiều cao 
day = float(input("Nhập đáy: "))
chieu_cao = float(input("Nhập chiều cao: "))

S = 1/2 * day * chieu_cao
print ('Diện tích tam giác là:', S)

# kiểm tra số nhập vào có phải số chẵn hay không
if day % 2 == 0:
    print(day, "là số chẵn")
else:
    print(day, "là số lẻ")

if chieu_cao % 2 == 0:
    print(chieu_cao, "là số chẵn")
else:
    print(chieu_cao, "là số lẻ")

# Viết chương trình tính lương tuần bằng cách nhập số giờ làm việc và lương mỗi giờ
gio_lam_viec = float(input("Nhập số giờ làm việc trong tuần: "))
luong_moi_gio = float(input("Nhập lương mỗi giờ: "))
luong_tuan = gio_lam_viec * luong_moi_gio
print("Lương tuần là:", luong_tuan)

# Viết chương trình tính số giấy sống được bằng cách nhập số năm. Ví dụ 100 năm = 3153600000 giây
so_nam_song = int (input("Nhập số năm sống:")) 
tong_so_giay_da_song = so_nam_song * 60 * 60 * 24 * 365
print("Tổng số giây đã sống là:", tong_so_giay_da_song)
