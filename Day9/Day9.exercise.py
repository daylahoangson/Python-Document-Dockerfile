## levle 1
## 1. Nhận đầu vào của người dùng bằng cách sử dụng input("Nhập tuổi của bạn: "). Nếu người dùng từ 18 tuổi trở lên, thì trả lời: Bạn đủ tuổi lái xe. Nếu dưới 18 thì cho biết còn bao nhiêu năm nữa mới đủ tuổi.
age = int(input ('Nhập tuổi của ban:'))
if age >= 18: 
    print ("Bạn đã đủ tuổi lái xe")
else: 
    age_reality = 18 - age
    print (f"Bạn còn {age_reality} năm nữa mới đủ tuồi lái xe.")
 ## 2. Cho người dùng nhập tuổi của họ và so sánh tuổi của bạn. Nếu tuổi bạn lớn hơn thì in ra bạn lớn hơn bao nhiêu tuổi và ngược lại.

my_age = 25 
age = int (input('Nhập tuổi của bạn:'))
a = my_age - age

if a > 0: 
    print ( f"Tôi lớn hơn bạn {a} tuổi")
elif a < 0:
    print (f"Bạn lớn hơn tôi {-a} tuổi")
else:
    print ( "Bạn bằng tuổi tôi")


## 3. Cho người dùng nhập a và b. Nếu a lớn hơn b in "a lớn hơn b", nếu a nhỏ hơn b thì in "a nhỏ hơn b".

a = input("Nhập số a:")
b = input("Nhập số b:")

if a > b:
    print ("a lớn hơn b")
else:
    print ("a nhỏ hơn b")

## Level 2
## 1. Cho học sinh nhập điểm và in điểm chữ. Ví dụ: 80-100=A, 70-79=B, 60-69=C, 50-59=D, 0-49=F.

point = int(input("Nhập điểm của bạn:"))

if 80 <= point <=100:
    print("Bạn được điểm A")
elif 70 <= point <= 79:
    print ("Bạn được điểm B")
elif 60 <= point <= 69:
    print ("Bạn được điểm C")
elif 50 <= point <= 59:
    print("Bạn được điểm D")
else: 
    print ("Bạn được điểm F")


## 2. Nhập tháng trong năm và cho biết tháng đó là mùa nào. Ví dụ Tháng 1-3 là mùa xuân, 4-6 là hạ, 7-9 là thu,10-12 là đông. 
month = int(input("Nhập tháng trong năm để kiểm tra:"))

if 1 <= month <=3: 
    print(" Đây là mùa Xuân")
elif 4<= month <= 6: 
    print ("Đây là màu Hạ")
elif 7<= month <= 9: 
    print ("Đây là mùa Thu")
else:
    print("Đây là mùa Đông")

## 3. Danh sách các loại trái cây gồm: fruits = ['banana','orange','mango', 'lemon']. Cho người dùng nhập trái cây, nếu không có trong list thì thêm vào, còn có rồi thì in "Trái cây đó đã có trong list".
fruits = ['banana','orange','mango', 'lemon']
fruits_input = input("Nhập tên trái cây:")
if fruits_input in fruits:
    fruits.add(fruits_input)
else:
    print("Trái cây đó đã có trong list")



