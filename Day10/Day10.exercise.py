## Bài tập 

## Level 1
## 1. In từ 0 đến 10 bằng vòng lặp for và while.
for i in range(11):
    print(i)
while i < 11:
    i = 0
    print(i)
    i += 1
## 2. In lại từ 10 đến 0 bằng vòng lặp for và while.
for i in range(10, -1, -1):
    print(i)
while i >= 0:
    i = 0
    print(i)
    i -= 1
## 3. Dùng vòng lặp để vẽ hình 
rows, cols = 6, 8  # đổi kích thước tại đây

for i in range(rows):
    for j in range(cols):
        print("#", end=" ")
    print()
## 4. Dùng vòng lặp để in bảng cửu chương như hình số 2

for i in range(11):
    print(f"{i} x {i} = {i * i}")
i = 0
while i <= 10 :
    print(f"{i} x {i} = {i * i}")
    i += 1
## 5. Dùng for để lặp từ 0 đến 100 và chỉ in các số chẵn.
for i in range(101):
    if i % 2 == 0:
        print(i)
## 6. Dùng for để lặp từ 0 đến 100 và chỉ in các số lẻ.
for i in range(101):
    if i % 2 != 0:
        print(i)

## level 2
##. 1 Sử dụng vòng lặp for để lặp từ 0 đến 100 và in tổng tất cả các số.
total = 0
for i in range(101):
    total += i
print("Tổng tất cả các số từ 0 đến 100 là:", total)

## 2 Sử dụng vòng lặp for để lặp từ 0 đến 100 và in ra tổng của tất cả các số chẵn và tổng của tất cả các số lẻ.
total_even = 0
total_odd = 0
for i in range(101):
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i
print("Tổng các số chẵn từ 0 đến 100 là:", total_even)
print("Tổng các số lẻ từ 0 đến 100 là:", total_odd)