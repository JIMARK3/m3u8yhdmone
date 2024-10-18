from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import json

executable_path = 'D:/chromedriver-win64/chromedriver.exe'
goods_url = 'https://yhdm.one/vod-play/2024334711/zheng_pian.html'
search_urls = [goods_url]

m3u8_url_dict = {i: [] for i in search_urls}
def get_m3u8_url(search_urls):
    for goods_url in search_urls:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        chrome_options.add_experimental_option('w3c', True)
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        service = Service(executable_path=executable_path)
        caps = DesiredCapabilities.CHROME
        caps["goog:loggingPrefs"] = {"performance": "ALL"}

        driver = webdriver.Chrome(service=service, options=chrome_options)  #

        # driver.set_page_load_timeout(10) # 这两种设置都进行才有效
        # driver.set_script_timeout(10)  # 这两种设置都进行才有效
        print("------------- LOGSTART -------------")
        # driver.implicitly_wait(8)
        # driver.maximize_window()
        print("minimize_window")
        driver.minimize_window()
        print("get " + goods_url)
        driver.get(goods_url)  #
        # 获取network请求
        print('get_log performance')
        logs = driver.get_log('performance')

        driver.close()
        print("------------- LOGSEND -------------")

        for log in logs:
            mesg = json.loads(log['message'])
            if not mesg.get('message') or not mesg['message'].get('params'):
                continue
            if mesg['message']['params'].get('response') and mesg['message']['params']['response'].get('url'):
                responseu = mesg['message']['params']['response']['url']
                m3u8_url_dict[goods_url].append(responseu)
            if mesg['message']['params'].get('url'):
                rqurls = mesg['message']['params']['url']
                m3u8_url_dict[goods_url].append(rqurls)
                # print(rqurls)
            if mesg['message']['params'].get('request') and mesg['message']['params']['request'].get('url'):
                requrls = mesg['message']['params']['request']['url']
                m3u8_url_dict[goods_url].append(requrls)
                # print(rpurls)
        result = {i: [] for i in search_urls}
        for search in m3u8_url_dict:
            for url in m3u8_url_dict[search]:
                if url.endswith('.m3u8') and url not in result[search]:
                    result[search].append(url)

        print(result)

get_m3u8_url(search_urls)