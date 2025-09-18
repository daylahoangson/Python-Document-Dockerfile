# 1. Nối chuỗi 'Ba muoi','ngay','hoc','Python' thành một chuỗi duy nhất,'Ba muoi ngay hoc Python'.
word1 = 'Ba mươi'
word2 = 'ngày'
word3 = 'học'
word4 = 'Python'
space = ' '
full_sentence = word1 + space + word2 + space + word3 + space + word4
print(full_sentence) # Ba mươi ngày học Python

#2. Thay đổi tất cả các ký tự thành chữ in hoa bằng phương thức upper().
print(full_sentence.upper()) 

# 3. Sử dụng các phương thức capitalize(), title(), swapcase() để định dạng giá trị của chuỗi Coding For All. 

challenge = 'Coding For All'
print(challenge.capitalize())
print(challenge.title())
print(challenge.swapcase())

# 4.  Kiểm tra xem chuỗi Coding For All có chứa từ Coding hay không bằng cách sử dụng phương thức index, find hoặc các phương thức khác.
challenge = 'Coding For All'
print(challenge.find('Coding'))
print(challenge.find('th'))

# 5. Tách chuỗi 'capitalize(), title(), swapcase()' bằng cách sử dụng split().
methods = 'capitalize(), title(), swapcase()'
print(methods.split(', '))

# 6. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" tách chuỗi trên bằng dấu phẩy.

challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (challenge.split(''))
challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (challenge.split(', '))

# 7. In các dòng dưới bằng cách định dạng chuỗi.

print(f"8 + 6 = 14 \n8 - 6 = 2 \n8 * 6 = 48 \n8 / 6 = 1.33 \n8 % 6 = 2 \n8 // 6 = 1 \n8 ** 6 = 262144")
