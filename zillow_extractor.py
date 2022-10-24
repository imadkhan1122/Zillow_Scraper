# ........................................Important Packages...................................#
import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import random
from fake_useragent import UserAgent


#-----------------------------Scraper function-----------------------------------------#
class SCRAPER:
    def __init__(self):
        self.main()
        
    def ZILLOW_SCRAPER(self, url='https://www.zillow.com/homedetails/2926-W-Kowalsky-Ln-Phoenix-AZ-85041/95179565_zpid/'):
        dic = {}
        # use header to send request with different agents to avoid blocking
        options = Options()
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
        driver = uc.Chrome(options=options)
        # Go to given URL
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        soup.text
        CONTAINER = soup.find('div', class_='layout-container')
        TEXT = CONTAINER.text
        TXT = TEXT.partition('more')[2]
        
        return TXT
    
    def main(self):
        urls = ['https://www.zillow.com/homedetails/19226-N-Cave-Creek-Rd-UNIT-111-Phoenix-AZ-85024/82829595_zpid/',
                'https://www.zillow.com/homedetails/3402-E-Indianola-Ave-Phoenix-AZ-85018/7565103_zpid/'
                ,'https://www.zillow.com/homedetails/2926-W-Kowalsky-Ln-Phoenix-AZ-85041/95179565_zpid/', 
                'https://www.zillow.com/homedetails/11666-N-28th-Dr-UNIT-264-Phoenix-AZ-85029/7750105_zpid/'
                ,'https://www.zillow.com/homedetails/2701-W-Griswold-Rd-Phoenix-AZ-85051/7751149_zpid/',
                'https://www.zillow.com/homedetails/2817-N-73rd-Dr-Phoenix-AZ-85035/95136918_zpid/', 
                'https://www.zillow.com/homedetails/3301-E-Kelton-Ln-UNIT-105-Phoenix-AZ-85032/2131070738_zpid/',
                'https://www.zillow.com/homedetails/6900-E-Princess-Dr-UNIT-2216-Phoenix-AZ-85054/68959861_zpid/']
        
        # Directly from dictionary
        print('[INFO] Downloading Data...')
        with open('Output.json', mode='w') as f:
            for url in urls:
                print(url)
                TXT = self.ZILLOW_SCRAPER(urls[1])
                print(TXT)
                # if dic['HOME-PRICE'] != '':
                #     f.write(json.dumps(dic, indent=2))
        
        print('[INFO] Downloaded')
        return
    
SCRAPER()