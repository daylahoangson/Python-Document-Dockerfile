# Bài tập 

# 1.Viết hàm đếm số dòng, số chữ trong file.
def count_lines_and_word (file):
    with open(file, 'r') as f:
        lines = f.readline()
        lines = f.readlines()
        word_count = sum(len(line.split()) for line in lines)
        return len(lines), word_count 
# 2. So sánh sự giống nhau của 2 file văn bản. Nó chỉ có 2 trạng thái là giống nhau hoàn toàn và không.
def compare_files(file1, file2):
    with open(file1,'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        return content1 == content2
# 3. Tạo 1 dictionary giới thiệu bản thân mình và chuyển nó sang jspn rồi lưu nó dưới dạng me.json
info_me = {
    "name": "Son pham",
    "age": 30,
    "city": "Ha Noi",
    "skill": "project manager",
    "email": "sonpham.work@gmail.com"
}
import json
with open('me.json', 'w') as json_file:
    json.dump(info_me, json_file)

# 4 Lấy 1 file bất kỳ, lập danh sách top 3 từ được dùng nhiều nhất. Đếm số dòng có từ đó. Tìm dòng có nhiều từ đó nhất.
def top_3_words(file):
    with open(file, 'r') as f:
        text = f.read()
        words = text.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        top_3 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
        return top_3
    
    