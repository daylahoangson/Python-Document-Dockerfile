letter = 'K' # Chuỗi có thể là một ký tự hoặc một văn bản 
print(letter) #K
print(len(letter)) #1
greening = 'Hello, world' # Chuỗi có thể nằm trong dấu nháy đơn ' ' hoặc dấu nháy kép " "
print(greening) # Hello , World 
print(len(greening)) # 12
sentence = "30 ngay học Python"
print (sentence) # 30 ngay học Python


# Chuỗi nhiều dòng 
multiline_string = '''Phython í a hight-level, general-purpose programming language. 
Ist design philosophy emphasize code readabilyty with the use ò singilicant via the of-side rule '''
print (multiline_string)

# Tương tự khác dấu """ """
multiline_string = """ Phython í a hight-level, general-purpose programming language.
 Ist design philosophy emphasize code readabilyty with the use ò singilicant via the of-side rule """
print (multiline_string)

first_name = 'Soon'
last_name = 'Pham'
space = ' '
full_name = first_name + space + last_name # Nối chuỗi
print(full_name) # Soon Pham

print (len (first_name)) # 4
print (len (last_name)) # 4
print (len (full_name)) # 9
print (len(first ) > len(last_name)) # False
print (len(first_name) < len(last_name)) # False
print (len(first_name) >= len(last_name)) # True
print (len(first_name) <= len(last_name)) # True
print (len(first_name) == len(last_name)) # True
print (len(first_name) != len(last_name)) # False


print( 'Hello\nWorld*) # Xuông dòng 
print( 'Thu thach \t30 ngay \thoc Python') # Thêm tab 
print( 'Dau gach cheo nguoc (\\)') # Thêm dầu gạch chéo ngược 
print( 'Dau nhay kep \"Hello, WorldI\"') # Dầu nhấy kép trong

# Chuỗi
first_name = 'Soon'
last_name = 'Pham'
language = 'Python'
formated_string = 'Tôi là %s %s. Tôi đang học %s' % (first_name, last_name, language)
print(formated_string) # Tôi là Soon Phham. Tôi đang học Python

# Chuỗi và số 
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'Diện tích hình tròn bán kính %d là %.2f' % (radius, area)# .2f: làm tròn 2 chữ số thập phân
print(formated_string) # Diện tích hình tròn bán kính 10 là 314.00

python_libraries = ['Django', 'Flask', 'NumPy', 'Pandas', 'Matplotlib', 'Python']
formated_string = 'Các thư viện Python phổ biến: %s' % (python_libraries)
print(formated_string) # Các thư viện Python phổ biến: ['Django', 'Flask', 'NumPy', 'Pandas', 'Matplotlib', 'Python']


