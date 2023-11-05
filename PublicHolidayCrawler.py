#General Imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Options for adding driver options
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options = options)
#Change depending upon your requirement
yearsToCrawl = ['2021','2022','2023']
#Change you country
country = 'nepal'
#Base url of the site to crawl data
baseUrl = f'https://www.officeholidays.com/countries/{country}/'
#File to store holidays
fileHolidays = open('Holidays.txt','w')
#Loops to interate number of years
for years in yearsToCrawl:
    #Creating final url by intergrating years
    finalUrl = baseUrl + years
    print(finalUrl)
    driver.get(finalUrl)
    time.sleep(2)
    #Getting time tag need to change if the site changes
    dates = driver.find_elements(By.TAG_NAME,'time')
    print(len(dates))
    for d in dates:
        holidayDate = d.get_attribute('datetime')
        fileHolidays.write(holidayDate)
        fileHolidays.write('\n')

driver.close()