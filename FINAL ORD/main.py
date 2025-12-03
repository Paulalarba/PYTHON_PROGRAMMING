from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://open-reaction-database.org/browse")

search = driver.find_element(By.ID, "search")
search.send_keys("Pauloy")
search.send_keys(Keys.RETURN)

time.sleep(10)
