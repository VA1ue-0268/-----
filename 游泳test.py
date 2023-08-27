import asyncio
import json
import requests
import datetime
import random
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry
from urllib.parse import unquote
from pyppeteer import launch

def login(user, pw):
    url = 'https://gym.sztu.edu.cn/api/users/auth'
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': 'https://gym.sztu.edu.cn',
    }
    data = {"username": user, "password": pw}

    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    cookie = eval(response.text)['data']['token']

    return cookie

async def qiang(cookie, id, num):
    cookies = { 'domain':'gym.sztu.edu.cn',
                'name':'token',
                'value':cookie}

    browser = await launch(headless=False)  # 开启浏览器
    page = await browser.newPage()
    await page.setCookie(cookies)

    # 进行操作
    await page.goto('https://gym.sztu.edu.cn/')  # 跳转
    await asyncio.sleep(2)
    await page.click('#app > div > div.van-swipe > div > div > div:nth-child(4) > button')
    await asyncio.sleep(1)
    await page.click('#app > div > div.van-popup.van-popup--round.van-popup--bottom > div > div.van-picker__toolbar > button.van-picker__confirm')
    await asyncio.sleep(1)

    while True:
        await page.click('#app > div > div.datebox > div > div:nth-child(2) > div.date-day.flex-center-center')
        await asyncio.sleep(0.5)
        class_name = await page.xpath(f'//*[@id="app"]/div/div[7]/div/div/div/div/div/div[2]/div[{num}]/div')
        # //*[@id="app"]/div/div[7]/div/div/div/div/div/div[2]/div[1]/div
        # //*[@id="app"]/div/div[7]/div/div/div/div/div/div[2]/div[2]/div
        #app > div > div.flex-stretch.box > div > div > div > div > div > div.relative.flex1 > div:nth-child(1) > div
        #app > div > div.flex-stretch.box > div > div > div > div > div > div.relative.flex1 > div:nth-child(2) > div
        # print(class_name)
        class_name = await (await class_name[0].getProperty("className")).jsonValue()
        if 'can_be_booked' in class_name:
            await page.click(f'#app > div > div.flex-stretch.box > div > div > div > div > div > div.relative.flex1 > div:nth-child({num}) > div')
            await asyncio.sleep(1)
            await page.click('#app > div > div.button-box > button:nth-child(2)')
            await asyncio.sleep(1)
            await page.click('#app > div > div.weChatPay-box > button')
            await asyncio.sleep(1)
            break
        else:
            print(time.strftime("%H:%M:%S", time.localtime()), id, class_name.split(' ')[-2])

    # await asyncio.sleep(1)
    # 获取滑块的尺寸
    box_num = 0
    while True:
        try:
            el = await page.querySelector(f'#nc_{box_num}_n1z')
            box = await el.boundingBox()
            # 鼠标悬浮在块上
            await page.hover(f'#nc_{box_num}_n1z')
            break
        except:
            print('fail:', box_num)
            box_num += 1
    # 按下鼠标
    await page.mouse.down()
    # 移动鼠标, 数字调试几次就知道了, 延迟设大点
    await page.mouse.move(box['x'] + 500, box['y'] + 5,{'delay': 1000, 'steps': 50})
    # 松开鼠标
    await page.mouse.up()
    await asyncio.sleep(10)
    await page.click('#app > div > button > div')
    await asyncio.sleep(1)
    # time.sleep(1)
    await browser.close()  # 关闭

# user_list = {'用户':'密码'}

cookies_list = []
user_list = {}
num_list = [1, 1, 1, 1, 1]

async def main():
    for i in user_list:
        cookies_list.append(login(i, user_list[i]))
    await asyncio.gather(*[qiang(i, j, k) for i, j, k in zip(cookies_list, user_list, num_list)])

if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(main())