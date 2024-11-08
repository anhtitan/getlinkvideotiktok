#author: anhtitan
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

username = "rongduatin"  # Thay thế user
output_folder = "D:/data_linkvideo"  
def get_latest_tiktok_links(username, num_videos=10):  # thay đổi số lượng link video cần lấy num_video=?
    # Khởi tạo Chrome driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    tiktok_url = f'https://www.tiktok.com/@{username}'
    driver.get(tiktok_url)

    # load video 15s
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/video/"]')))
    time.sleep(5)  # load trang

    # get link video
    video_links = []
    videos = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/video/"]')
    for video in videos[:num_videos]:
        link = video.get_attribute('href')
        video_links.append(link)


    driver.quit()

    return video_links


links = get_latest_tiktok_links(username)

def get_unique_file_name(file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1

    while os.path.exists(file_name):
        file_name = f"{base_name}({counter}){extension}"
        counter += 1

    return file_name

# lưu
file_name = f"{username}.txt"
file_name = get_unique_file_name(os.path.join(output_folder, file_name))  


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


with open(file_name, "w") as file:
    for link in links:
        file.write(link + "\n")

print(f"Link 10 video của kênh '{username}' đã được lưu ở '{file_name}'")
