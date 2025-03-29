from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://google.com")
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "some_id"))
)

time.sleep(5)
driver.quit()
