import random
import string


# Cấu hình
num_usernames = 100  # Số lượng email cần tạo
length = 15  # Độ dài của phần username trước @
domain = "imail.edu.vn"  # Domain email

last_names = [
    'nguyen', 'pham', 'le', 'tran', 'hoang', 'do', 'vu', 'bui', 'ngo', 'dinh',
    'cao', 'mai', 'hanh', 'dang', 'pham', 'ly', 'huynh', 'la', 'quach', 'ngoc',
    'vuong', 'luu', 'phung', 'vuong', 'ho', 'trieu', 'chien', 'tang', 'kim', 
    'ngai', 'dong', 'bu', 'to', 'quang', 'chu', 'duong', 'vong', 'hoang', 'luong',
    'nguyenhieu', 'dai', 'chung', 'diem', 'thuong', 'tranthao', 'vansang'
]

first_names = [
    'van', 'hoang', 'thanh', 'khanh', 'ngoc', 'lien', 'tung', 'trang', 'lan', 'dung', 
    'thao', 'tuan', 'minh', 'tam', 'bao', 'hieu', 'dong', 'diem', 'lanh', 'nhung', 
    'bich', 'thu', 'dao', 'ly', 'quyen', 'hang', 'nhan', 'phu', 'duong', 'mau', 
    'nhat', 'toan', 'hieu', 'trieu', 'quang', 'my', 'trang', 'quyen', 'xuan', 'an', 
    'tho', 'sang', 'nam', 'huy', 'dai', 'kieu', 'nhi', 'minhchau', 'thuy', 'le', 
    'lan', 'xuan', 'quyen', 'thuy'
]

def generate_random_usernames(num_usernames, length, domain):
    usernames = set()  # Sử dụng set để tự động loại bỏ tên trùng lặp
    
    while len(usernames) < num_usernames:
        # Chọn ngẫu nhiên một họ và một tên
        last_name = random.choice(last_names)
        first_name = random.choice(first_names)
        
        # Ghép họ và tên thành một phần của tên người dùng
        base_username = last_name + first_name
        
        # Nếu tên người dùng ngắn hơn độ dài yêu cầu, thêm ký tự ngẫu nhiên vào cuối
        if len(base_username) < length:
            # Tạo chuỗi ngẫu nhiên gồm chữ cái thường và chữ số để bổ sung vào cuối
            random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length - len(base_username)))
            base_username += random_suffix
        else:
            # Nếu tên người dùng đã đủ dài, cắt bớt để đúng độ dài
            base_username = base_username[:length]
        
        # Tạo email từ tên người dùng và domain
        email = f"{base_username}@{domain}"
        
        # Thêm vào set (set tự động loại bỏ sự trùng lặp)
        usernames.add(email)
    
    return list(usernames)


# Tạo danh sách email
usernames = generate_random_usernames(num_usernames, length, domain)

# In kết quả
for username in usernames:
    print(username)

# lưu vào file
with open("emails.txt", "w") as file:
    file.write("\n".join(usernames))

print("lưu vào file emails.txt")

