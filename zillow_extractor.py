from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

#-----------------------------Scraper function-----------------------------------------#
class SCRAPER:
    def __init__(self):
        self.main()
        
    def ZILLOW_SCRAPER(self, url):
        dic = {}
        # use header to send request with different agents to avoid blocking
        hdr = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
              }
        # send request to url
        r = Request(url,headers=hdr)
        # visiting html page
        page = urlopen(r)
        # check while page status code not equal to 200
        while page.getcode() != 200:
            page = urlopen(r)
           
        soup = BeautifulSoup(page, 'html.parser')
        
        CONTAINER = soup.find('div', attrs={"role": "dialog"})
        
        try:
            # Media Section
            CONT_MEDIA = CONTAINER.find('div', class_='ds-media-col ds-media-col-hidden-mobile')
            # Data Section
            CONT_DATA = CONTAINER.find('div', class_='ds-data-col ds-white-bg ds-data-col-data-forward')
            
            CONT_SUMMARY = CONT_DATA.find('div', class_='hdp__sc-1tsvzbc-1 ds-chip')
            
            CONT_SUMM_DATA = CONT_SUMMARY.find('div', class_='ds-home-details-chip')
            
            BED_BATH_AREA_CONT_BOX = CONT_SUMM_DATA.find('div', class_='ds-summary-row')
            
            HOME_PRICE = BED_BATH_AREA_CONT_BOX.find('span', class_='Text-c11n-8-63-0__sc-aiai24-0 hdp__sc-b5iact-0 cfVcI fAzOKk').text
            
            BED_BATH_AREA_CONT = BED_BATH_AREA_CONT_BOX.find('div', class_='ds-bed-bath-living-area-header')
            
            BED_BATH_AREA = BED_BATH_AREA_CONT.find('span', class_='ds-bed-bath-living-area-container')
            
            BED_BATH_AREA_ = BED_BATH_AREA.find_all('span', class_='hdp__sc-rfpg3m-0 bqcSTm')
            
            BED = BED_BATH_AREA_[0].text
            
            BATH = BED_BATH_AREA_[1].text
            
            AREA = BED_BATH_AREA_[2].text
            
            ADDRESS = CONT_SUMM_DATA.find('h1', id='ds-chip-property-address').text
            
            STATUS = CONT_SUMM_DATA.find('div', class_='hdp__sc-11h2l6b-2 dMJElH ds-chip-removable-content').text
            dic = {'HOME-PRICE':HOME_PRICE, 'BED-ROOMS':BED, 'BATH-ROOMS':BATH, 'SQ-AREA':AREA, 'LOCATION':ADDRESS, 'STATUS':STATUS}
        except:          
            dic = {'HOME-PRICE':'', 'BED-ROOMS':'', 'BATH-ROOMS':'', 'SQ-AREA':'', 'LOCATION':'', 'STATUS':''}
        # CONT_DATA_VIEW = CONT_DATA.find('div', class_='data-view-container')
        
        return dic
    
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
                dic = self.ZILLOW_SCRAPER(urls[1])
                print(dic)
                if dic['HOME-PRICE'] != '':
                    f.write(json.dumps(dic, indent=2))
        
        print('[INFO] Downloaded')
        return
    
SCRAPER()