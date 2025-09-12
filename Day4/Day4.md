### Chuỗi 
 Văn bản là một kiểu dữ liệu chuỗi. Bất kỳ loại dữ liệu nào được viết dưới dạng văn bản đều là chuỗi. Python có các phương thức chuỗi khác nhau và các hàm có sẵn để xử lý các chuỗi. Để kiểm tra độ dài của chuỗi, bạn có thể dử dụng hàm **len()**.

 ![alt text](image.png)

 ![alt text](image-1.png)

 ## Nối chuỗi 
 Bạn có thể nối 2 hoặc nhiều chuỗi lại với nhau bằng cách dưới đây. Ngoài ra bạn có thể sử dụng **join()** thay vì + để việc nối chuỗi hiệu qủa hơn. 

 ![alt text](image-2.png)

 ## Escape sequence 

 Trong Python và các ngôn ngữ khác, cú pháp **\{ký tự}** là Escape sequenc. Các Escape sequenc phổ biên nhất 
 - \n: Tạo dòng mới 
 - \t: Thêm tab(8 dấu cách) 
 - \\: Dấu gạch chéo ngược
 - \': Dấu nháy đơn (') 
 - \": Dấu nháy kép 

 ![alt text](image-3.png)

 ## Định dạng chuỗi 

 Toán tử **"%"** được sử dụng để định dạng một tập hợp các biến được đặt trong một **"tuple"**. cùng với đối số là các ký hiệu đặc biệt như "%s", "%d", "%f", "%.nf":
 - **%s** - Chuỗi 
 - **%d** - Số nguyên 
 - **%f** - Số thực
 - **%.nf** - Số thực với độ chính xác n

![alt text](image-4.png)

**Định dạng chuỗi này được giứoi thiệu trong python python3**

![alt text](image-5.png)

## Nội suy chuỗi 

Một định dạng chuỗi mới khác là nội suy chuỗi, **F-string**. Các chuỗi bắt đầu bằng f và chúng ta có thể đưa dữ liệu vào các vị trí tương đương trong chuỗi.

![alt text](image-6.png)

## Chuỗi dưới dạng các ký tự 

Chuỗi Python là **Tập hợp các ký tự**. Cách đơn giản nhất đẻ trích xuất các ký tự đơn lẻ từ các chuỗi là gán chúng vào các biến tương ứng. 

![alt text](image-7.png)

## Truy cập ký tự thoe index

Trong lập trình thứ tự đếm **bắt đầu từ số 0** Do đó, chữ cái đầu tiên của chuỗi có index bằng 0 và chữ cái cuối cùng của chuỗi là độ dài của chuỗi trừ đi một. 

![alt text](image-8.png)

![alt text](image-9.png)

## Cắt chuỗi 

Trong Python, chúng ta có thể cắt các chuỗi thành các chuỗi con.

![alt text](image-10.png)

## Đảo ngược chuỗi 

Chúng ta có thể dễ dàng đảo ngược chuỗi trong Python bằng cách dưới. 

![alt text](image-11.png)

## Bỏ qua ký tự khi cắt chuỗi 

Bạn có thể bỏ qua các ký tự không mong muốn bằng cách thêm bước nhảy khi cắt chuỗi. 

![alt text](image-12.png)

## Phương thức 
**capitalize()**: Chuyển ký tự đầu tiên của chuỗi thành chữ in hoa.

![alt text](image-13.png)

**count()**: tar về số lần xuất hiện của chuỗi con trong chuỗi, đếm (chuỗi co, bắt đầu từ, kết thúc).  

![alt text](image-14.png)

**endwith**: Kiểm tra xem một chuỗi có kết thúc bằng một từ được chỉ định hay không. 

![alt text](image-15.png)

**expandtabs**: Thay thế ký tự tab bằng dấu cách, kích thước tab mặc định là 8. 

![alt text](image-16.png)

**find()**: Trả về index của lần xuất hiện đầu tiên của chuỗi con, nếu không tìm thấy trả về -1. 

![alt text](image-17.png)

**rfind()**: Trả về index của lần xuất hiện cuối cùng của chuỗi con, nếu không tìm thấy trả về -1. 

![alt text](image-18.png)

**index**: Trả về index thấp nhất của một chuỗi con,các tham số cho biết vị trí bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi -1). Nếu không tìm thấy chuỗi con, nó sẽ trả giá trị Error.

![alt text](image-19.png)

**rindex**: Trả về index cao nhất của một chuỗi con, các tham số bổ sung cho biết vị trí bắt đầu và kết thúc (mặc định 0 và độ dài chuỗi -1).

![alt text](image-20.png)

**isalnum**: Kiểm tả ký tự chữ và số.

![alt text](image-21.png)

**isalpha()** Kiểm tra xem tất cả các phần tử trong các chuỗi có phải là ký tự trong bảng chữ cái hay không (a-z và A-Z).

![alt text](image-22.png)

**isdigt()**: Kiểm tra tất cả các ký tự trong chuỗi có phải là số không (0-9 và một số ký tự unicode khác cho số). 

![alt text](image-23.png)

**isnumeric()**: Kiểm tra xem tất cả các ký tự trong chuỗi có phải là số hoặc liện quan đến số hay không (giống như insdigit(), nhưng chấp nhận nhiều dạng hơn, như 1/2)

![alt text](image-24.png)

**isdentifile()**: Kiểm tra xem một chuỗi có phải là một tên biến hợp lệ hay không. 

![alt text](image-25.png)

**islower()**: Kiểm tra xem tất cả xá ký tự trong chuỗi có phải là chữ thường hay không. 

![alt text](image-26.png)

**isupper()**: Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ hoa hay không. 

![alt text](image-27.png)

**join()**: Nối các chuỗi lại với nhau. 

![alt text](image-28.png)

**strip()**: Xoá tất cả các ký tự được chỉ định trong đầu và cuối mỗi chữ. 

![alt text](image-29.png)

**replace()**: Thay thế chuỗi con bằng một chuỗi đã cho. 

![alt text](image-30.png)

**split()**: Tách chuỗi, sử dụng chuỗi hoặc khoảng trắng đã cho làm thư ký tự phân cách. 

![alt text](image-31.png)

**title()** Trả về tiêu đề chuỗi. 

![alt text](image-32.png)

**sawpcase()**: Chuyển đổi tất cả các ký tự hoa thành ký tự thường và tất cả ký tự thường thành ký tự hoa. 

![alt text](image-33.png)

**startedwith()**: Kiểm tra xem chuỗi có bắt đầu bằng chuỗi được chỉ định hay không. 

![alt text](image-34.png)

## Bài tập 

1. Nối chuỗi 'Ba muoi','ngay','hoc','Python' thành một chuỗi duy nhất,'Ba muoi ngay hoc Python'.
2. Thay đổi tất cả các ký tự thành chữ in hoa bằng phương thức upper().
3. Sử dụng các phương thức capitalize(), title(), swapcase() để định dạng giá trị của chuỗi Coding For All. Kiểm tra xem chuỗi Coding For All có chứa từ
4. Coding hay không bằng cách sử dụng phương thức index, find hoặc các phương thức khác.
5. Tách chuỗi 'capitalize(), title(), swapcase()' bằng cách sử dụng split().
6. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" tách chuỗi trên bằng dấu phẩy.
7. In các dòng dưới bằng cách định dạng chuỗi.

