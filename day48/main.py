from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome()
driver.get("https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/B09MZTP44L?th=11")
price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_cents=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print(f"The price i  {price_dollar.text}.{price_cents.text}")
driver.quit()