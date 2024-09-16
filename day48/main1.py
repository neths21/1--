from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
dates=driver.find_elements( by=By.CSS_SELECTOR,value='.event-widget last time')
for i in dates:
    print(i.text)
driver.close()
