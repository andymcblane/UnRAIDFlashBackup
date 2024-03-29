from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import os 

driver = None

try:
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    WEB_URL = os.environ["WEB_URL"]
    HUB_URL = os.environ["HUB_URL"]
    BACKUP_FREQUENCY_SECS = int(os.environ["BACKUP_FREQUENCY_SECS"])
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
        driver.find_element("xpath", "//input[@name='password']").send_keys(PASSWORD)
        driver.find_element("xpath", "//input[@name='password']").submit()
        driver.get(f"{WEB_URL}/Main/Settings/Flash?name=flash")
        time.sleep(2)
        driver.find_element("xpath", "//input[@value='Flash backup']").click()
        time.sleep(60 * 5)
        try:
            driver.quit()
        except Exception as e:
            print(str(e))
        time.sleep(BACKUP_FREQUENCY_SECS)

finally:
    if driver is not None:
        driver.quit()