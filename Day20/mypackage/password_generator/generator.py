#mypackage/password.py

import random
import string

def generate_password(length):
    if length < 3:
        raise ValueError("Độ dài mật khẩu phải >= 3")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Bắt buộc có ít nhất 1 ký tự mỗi loại
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    # Các ký tự còn lại
    all_chars = lowercase + uppercase + digits
    password += random.choices(all_chars, k=length - 3)

    # Trộn thứ tự
    random.shuffle(password)

    return ''.join(password)
