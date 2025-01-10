import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)

chrome_options = Options()
options.add_argument(f"--user-agent={user_agent}")
options.add_argument("--window-size=2560,1440")

# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless=new")  # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
start_url = (
    "https://flatmates.com.au/"  # "share-houses/sydney/males+private-room?page=1"
)

driver.get(start_url)
# driver.find_element_by_class_name("gdpr-consent-element-button").click()
time.sleep(10)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# s = driver.find_elements(
#     By.XPATH,
#     "//div[text()='See more']",
# )
# tag = "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1sur9pj xkrqix3 xzsf02u x1s688f"
# time.sleep(3)


print(driver.page_source)
# b'<!DOCTYPE html><html xmlns="http://www....
driver.quit()
