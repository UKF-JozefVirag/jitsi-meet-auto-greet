from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

name = input("Enter name: ")
meet_link = "https://meet.ukf.sk/" + input("Enter room: ")
greet = "Dobrý deň"
goodbye = "Dovidenia"

opt = Options()

opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })


driver = webdriver.Chrome(r'C:\Users\drivers\chromedriver.exe',  chrome_options=opt)
driver.maximize_window()
driver.get(meet_link)

driver.find_element_by_xpath('//*[@id="videoconference_page"]/div[5]/div[1]/div/div/div[1]/input').send_keys(name, u'\ue007')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="new-toolbox"]/div/div/div/div[4]/div/div/div').click()
driver.find_element_by_xpath('//*[@id="usermsg"]').send_keys(greet, u'\ue007')

while True:
    time.sleep(10)
    if (driver.page_source.__contains__("dovidenia") or driver.page_source.__contains__("Dovidenia")):
        driver.find_element_by_xpath('//*[@id="usermsg"]').send_keys(goodbye, u'\ue007')
        time.sleep(3)
        break

driver.close()

