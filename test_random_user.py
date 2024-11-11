import random
import string

def generate_random_usernames(num_usernames=100, length=10, domain="imail.edu.vn"):
    usernames = []
    for _ in range(num_usernames):
        # Tạo một chuỗi ngẫu nhiên chỉ gồm chữ cái thường, với độ dài tùy chỉnh
        random_username = ''.join(random.choices(string.ascii_lowercase, k=length))
        email = f"{random_username}@{domain}"
        usernames.append(email)
    return usernames

# Cấu hình
num_usernames = 100  # Số lượng email cần tạo
length = 10  # Độ dài của phần username trước @
domain = "imail.edu.vn"  # Domain email

# Tạo danh sách email
usernames = generate_random_usernames(num_usernames, length, domain)

# In kết quả
for username in usernames:
    print(username)

# Hoặc lưu vào file
with open("emails.txt", "w") as file:
    file.write("\n".join(usernames))

print("Generated emails saved to emails.txt")
