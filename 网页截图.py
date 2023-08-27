from PIL import Image
from io import BytesIO
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = ""


def get_cookie_list(cookie):
    """
    :param : 从浏览器cv的或者去从requests里获取到的cookie
    :return:       反回cookie列表
    """
    cookie_list = []
    
    for i in cookie.split(';'):
        i_dict = {'name': i.split('=')[0].strip(), 'value': i.split('=')[1].strip()}
        cookie_list.append(i_dict)

    return cookie_list

def save_screenshot(driver, file_name):
    element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'reading-right-wrapper')))

    analysis_list = element.find_elements(By.CLASS_NAME, "multi-columns")
    for i in analysis_list:
        driver.execute_script('arguments[0].setAttribute("style", "")', i)
        
    analysis_list = element.find_elements(By.CLASS_NAME, "checkbox")
    for i in analysis_list:
        driver.execute_script('arguments[0].setAttribute("style", "")', i)

    analysis_list = element.find_elements(By.CLASS_NAME, "analysis__controll")
    for i in analysis_list:
        driver.execute_script("arguments[0].click();", i)

    analysis_list = element.find_elements(By.CLASS_NAME, "hidden")
    for i in analysis_list:
        print(i.get_attribute('class'))
        driver.execute_script('arguments[0].className="items-wrap"', i)
        

    analysis_list = element.find_elements(By.CLASS_NAME, "title")
    for i in analysis_list:
        print(i.get_attribute('class'))
        driver.execute_script('arguments[0].className="title show-options"', i)

    height = driver.execute_script('return document.querySelector("#reading-right-wrapper > div.scroller").clientHeight')
    # width = driver.execute_script('return document.querySelector("#reading-right-wrapper > div.scroller").clientWidth')
    width = 2560
    driver.set_window_size(width, height)
    time.sleep(1)
    img_binary = element.screenshot_as_png
    img = Image.open(BytesIO(img_binary))
    print(file_name)
    img.save(file_name+".png")
    print(" screenshot saved ")

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(2560, 1440)
driver.get("https://ieltscat.xdf.cn/")
for i in get_cookie_list(cookie):
    print(i)
    driver.add_cookie(i)

driver.get("https://ieltscat.xdf.cn/practice/read")

books = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]')))
books = books.find_elements(By.XPATH, ".//*")

for i in range(len(books)):
    print(i)
    books[i].click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/div[2]/div[2]')))
    time.sleep(1)
    for test in range(1, 5):
        for passage in range(1, 4):
            to_click = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/table[{test}]/tbody/tr[{passage}]/td[7]')))
            to_click.click()
            handles = driver.window_handles
            driver.switch_to.window(handles[1])
            # try:
            #     to_click = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[3]/div[3]")))
            #     to_click.click()
            # except:
            #     pass
            
            driver.set_window_size(2560, 1440)
            to_click = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/p[4]/button")))
            to_click.click()
            handles = driver.window_handles
            driver.switch_to.window(handles[2])
            save_screenshot(driver, f"book{17-i} test{test} passage{passage}")
            driver.close()
            driver.switch_to.window(handles[1])
            driver.close()
            driver.switch_to.window(handles[0])
