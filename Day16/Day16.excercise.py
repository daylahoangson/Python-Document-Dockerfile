## Bài tập 
## 1. Lấy ngày, tháng, năm, giờ, phút và timestamp hiện tại từ module datetimebn.  

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Giờ hiện tại:", current_time)

## 2. Định dạng ngày hiện tại bằng định dạng sau: "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Ngày hiện tại:", formatted_date)

## 3. Chuyển chuỗi "14 June, 2023" sang datetime.
date_string = "14 June, 2023"
converted_date = datetime.strptime(date_string, "%d %B, %Y")
print("Ngày đã chuyển đổi:", converted_date)

## 4. Tính thời gian từ giờ đến năm mới còn bao nhiêu lâu nữa 
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
time_left = new_year - now
print("Thời gian còn lại đến năm mới:", time_left)

## 5. Tính thời gian từ ngày 1 tháng 1 năm 1970 đến hiện tại. 
epoch = datetime(1970, 1, 1)
time_since_epoch = now - epoch
print("Thời gian từ 1/1/1970 đến hiện tại:", time_since_epoch)


