from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Danh sách các username bạn muốn lấy video
# usernames = ["rongduatin", "theanh28entertainment", "rodgri_team_1995"]  # Thay đổi danh sách này theo nhu cầu của bạn
def read_usernames_from_file(file_path):
    usernames = []
    try:
        with open(file_path, 'r') as f:
            # Đọc tất cả dòng và loại bỏ khoảng trắng dư thừa
            usernames = [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Lỗi khi đọc tệp {file_path}: {e}")
    return usernames

# Đường dẫn tới tệp username.txt chứa danh sách các tài khoản TikTok
username_file_path = "username.txt"

# Đọc danh sách username từ tệp
usernames = read_usernames_from_file(username_file_path)
output_folder = "C:/data_linkvideo"  # Thư mục lưu trữ các liên kết video


# Hàm lấy liên kết video từ một tài khoản TikTok
def get_latest_tiktok_links(username, num_videos=10): 
    # Khởi tạo Chrome driver với hồ sơ người dùng mặc định
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument("--headless")  # Chạy trình duyệt ở chế độ nền
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    tiktok_url = f'https://www.tiktok.com/@{username}'
    driver.get(tiktok_url)

    try:
        # Chờ cho đến khi phần tử video xuất hiện
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/video/"]')))
    except Exception as e:
        print(f"Không thể tìm thấy phần tử video sau 10 giây chờ đợi cho username {username}: {e}")
        driver.quit()
        return []

    print(f" TikTok của {username} đã tải xong.")
    time.sleep(3)  # Thêm thời gian chờ để tải video

    # Cuộn trang để tải thêm video
    # scroll_to_load_more_videos(driver)

    # Lấy các liên kết video
    video_links = []
    videos = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/video/"]')

    # print(f"Tìm thấy {len(videos)} video trên trang của {username}.")  # In số video tìm thấy

    # Lấy tối đa num_videos video
    for video in videos[:num_videos]:
        link = video.get_attribute('href')
        video_links.append(link)
        time.sleep(1)  # Thêm một chút thời gian chờ sau mỗi lần lấy link video

    driver.quit()

    return video_links

# Hàm để tạo tên file duy nhất nếu đã tồn tại
def get_unique_file_name(file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1

    while os.path.exists(file_name):
        file_name = f"{base_name}({counter}){extension}"
        counter += 1

    return file_name

# Lặp qua các username và lấy video
for username in usernames:
    try:
        # Lấy liên kết video cho từng tài khoản
        links = get_latest_tiktok_links(username)

        # Tạo tên file cho mỗi username
        file_name = f"{username}.txt"
        file_name = get_unique_file_name(os.path.join(output_folder, file_name))  

        # Tạo thư mục nếu chưa có
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Lưu các liên kết vào file
        with open(file_name, "w") as file:
            for link in links:
                file.write(link + "\n")

        print(f"Link 10 video của kênh '{username}' đã được lưu ở '{file_name}'")
    except Exception as e:
        print(f"Đã có lỗi khi lấy video cho username '{username}': {e}")
