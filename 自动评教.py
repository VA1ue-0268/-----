import os
import random
import asyncio

from pyppeteer import launch
from pyppeteer.dialog import Dialog

async def jiaoping(user:str, passwd:str, delay:float):
    browser = await launch(headless=False)  # 开启浏览器
    page = await browser.newPage()
    
    # 进行操作
    await page.goto('https://jwxt.sztu.edu.cn/')  # 跳转

    await page.type('#j_username', user)
    await page.type('#j_password', passwd)

    await page.click('#loginButton')

    while True:
        try:
            await page.click('#zccd > div.edu-aside > header')
            break
        except:
            pass

    await page.click('#accordion > li:nth-child(11) > div')
    await asyncio.sleep(0.5)
    await page.click('#accordion > li.open > ul > li > div')
    await asyncio.sleep(0.5)
    await page.click('#accordion > li.open > ul > li > ul')
    await asyncio.sleep(1)

    for frame in page.frames:
        for childFrame in frame.childFrames:
            try:
                for t in [2, 3]:
                    await childFrame.click(f'#Form1 > table > tbody > tr:nth-child({t}) > td:nth-child(8) > a')
                    await asyncio.sleep(2)
                    try:
                        for i in range(2, 21):
                            if '否' in await (await (await childFrame.xpath(f'//*[@id="dataList"]/tbody/tr[{i}]/td[6]'))[0].getProperty('textContent')).jsonValue():
                                await childFrame.click(f'#dataList > tbody > tr:nth-child({i}) > td:nth-child(8) > a')
                                await asyncio.sleep(1)
                                try:
                                    for j in range(3, 36, 2):
                                        await childFrame.click(f'#table1 > tbody > tr:nth-child({j}) > td:nth-child(2) > label:nth-child(1)')
                                        await asyncio.sleep(random.uniform(0.5, 0.6 + delay))
                                except:
                                    pass
                                await childFrame.click(f'#table1 > tbody > tr:nth-child(13) > td:nth-child(2) > label:nth-child(3)')
                                await asyncio.sleep(random.uniform(0.5, 0.6 + delay))
                                await childFrame.click(f'#bc')
                                page.on('dialog', lambda dialog: asyncio.ensure_future(dialog.dismiss()))
                                await asyncio.sleep(3)
                    except:
                        pass
                    await childFrame.click('#btnShenshen')
                    await asyncio.sleep(1)
                break
            except:
                pass

    os.system("cls")
    print('！！脚本仅保存结果，需手动提交！！')
    print('By VA1ue')
    os.system('pause')

if __name__ == '__main__':
    user = input('账号:')
    pw = input('密码:')
    delay = float(input('延迟（单位s，越小选择速度越快）：'))
    asyncio.get_event_loop().run_until_complete(jiaoping(user, pw, delay))