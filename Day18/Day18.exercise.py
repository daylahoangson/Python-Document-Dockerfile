# Bài tập 

# 1. Thống kê số lần các từ xuất hiện trong đoạn sau:
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

word_count = {}
for word in paragraph.split():
    word = word.lower().strip('.,')
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

#2. Kiểm tra 1 chuỗi có phải là 1 biến hợp lệ hay không.

is_valid_variable("first_name")
is_valid_variable("first-name")
is_valid_variable("1st_name")
is_valid_variable("firstname")
is_valid_variable("first name")

# 3 làm sạch chuỗi dưới và tìm 3 từ xuất hiện nhiều nhất

sentence = '''%I $am@% a stea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting Sand& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Dodes thi%s mo@tivate you to be a tea@cher!?'''
def most_frequent_words(text):
    # Làm sạch chuỗi
    cleaned_text = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text)
    words = cleaned_text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    # Tìm 3 từ xuất hiện nhiều nhất
    most_frequent = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
    return most_frequent

print (most_frequent_words(sentence)) 