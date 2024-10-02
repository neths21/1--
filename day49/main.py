from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3908887401&f_AL=true&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true")
sign_inpage=driver.find_element(By.LINK_TEXT,value="Sign in")
sign_inpage.click()
