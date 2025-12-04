import os
import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

BASE_URL = "https://open-reaction-database.org"

if not os.path.exists("ORD_DATA"):
    os.makedirs("ORD_DATA")

driver.get(f"{BASE_URL}/browse")
time.sleep(3)

dataset_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/dataset/']")
dataset_urls = list({link.get_attribute("href") for link in dataset_links})

print("Found dataset count:", len(dataset_urls))

def scrape_tab(tab_name, dataset_folder):

    try:
        tab = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                f"//div[contains(@class,'tab') and contains(text(), '{tab_name}')]"))
        )
        tab.click()
        time.sleep(1)

    except:
        print(f"Tab {tab_name} not found.")
        return

    tab_folder = f"{dataset_folder}/{tab_name.lower().replace(' ', '_')}"
    if not os.path.exists(tab_folder):
        os.makedirs(tab_folder)

    cards = driver.find_elements(By.CSS_SELECTOR, ".card")

    print(f"  {tab_name}: {len(cards)} items found")

    for i, card in enumerate(cards, start=1):
        try:
            card.click()
            time.sleep(0.5)

            raw_pre = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "pre"))
            )
            raw_text = raw_pre.text.strip()

            fname = f"{tab_folder}/raw_{i}.txt"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(raw_text)

            print(f"    ✓ Saved {tab_name} raw_{i}.txt")

        except Exception as e:
            print(f"    ✗ Failed to extract item {i}: {e}")
            continue


for dataset_url in dataset_urls:

    driver.get(dataset_url)
    time.sleep(2)

    dataset_id = dataset_url.split("/")[-1]
    print("\nProcessing dataset:", dataset_id)

    dataset_folder = f"ORD_DATA/{dataset_id}"
    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)

    # SCRAPE EACH MATERIAL CATEGORY
    scrape_tab("Base", dataset_folder)
    scrape_tab("Solvent", dataset_folder)
    scrape_tab("amine", dataset_folder)
    scrape_tab("aryl halide", dataset_folder)
    scrape_tab("metal and ligand", dataset_folder)

driver.quit()
print("\nALL DATASETS SCRAPED SUCCESSFULLY!")
