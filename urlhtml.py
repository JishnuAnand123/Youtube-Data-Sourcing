import html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import httpx
import asyncio


def get_youtube_html(driver,url):
    #print("get_details")
    #driver = webdriver.Chrome()    
    driver.get(url)
    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.END)
    time.sleep(2)
    html.send_keys(Keys.END)
    time.sleep(1)
    html.send_keys(Keys.END)
    time.sleep(1)
    html.send_keys(Keys.END)
    time.sleep(2)
    content = driver.page_source.encode('utf-8').strip()
    return content


async def get_html_async(urls):
    async with httpx.AsyncClient(timeout=None) as client:

        tasks=(client.get(url) for url in urls)
        regs = await asyncio.gather(*tasks)

    htmls=[reg.text for reg in regs]   

    return htmls









