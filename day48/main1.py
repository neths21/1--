from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
times=driver.find_elements( by=By.CSS_SELECTOR,value='.event-widget time')
names=driver.find_elements( by=By.CSS_SELECTOR,value='.event-widget li a')
events={}
for n in range(len(times)):
    events[names[n].text]=times[n].text
for i in times:
    print(i.text)
driver.close()
print(events)