from selenium import webdriver
import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(100)

browser.get("https://open-reaction-database.org/")
time.sleep(9999)