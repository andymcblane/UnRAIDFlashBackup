import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
import json 
from selenium.common.exceptions import ElementClickInterceptedException
import subprocess
from pathlib import Path
import os 

try:
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    WEB_URL = os.environ["WEB_URL"]
    HUB_URL = os.environ["HUB_URL"]
    BACKUP_FREQUENCY_SECS = os.environ["BACKUP_FREQUENCY_SECS"]
    while True:
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
          "download.default_directory": "/mnt/flash_backups/",
          "download.prompt_for_download": False,
          "download.directory_upgrade": True,
          "safebrowsing.enabled": True
        })
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-crash-reporter")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-in-process-stack-traces")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument('--disable-dev-shm-usage')        

        driver = webdriver.Remote(HUB_URL, options=chrome_options)

        driver.get(WEB_URL)

        driver.find_element("xpath", "//input[@name='username']").send_keys(USERNAME)
        driver.find_element("xpath", "//input[@name='password']").send_keys(PASSWORD).submit()
        driver.get(f"{WEB_URL}/Main/Settings/Flash?name=flash")
        time.sleep(2)
        driver.find_element("xpath", "//input[@value='Flash backup']").click()
        driver.quit()
        time.sleep(BACKUP_FREQUENCY_SECS)

finally:
    driver.quit()