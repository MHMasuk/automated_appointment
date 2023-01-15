from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


def get_driver(headless):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")

    # initialize driver
    driver = webdriver.Chrome(
        executable_path=Path(BASE_DIR).joinpath('../chromedriver.exe'),
        chrome_options=options)
    return driver


def connect_to_base(browser):
    # base_url = "https://ezov.mzv.sk/e-zov/"
    base_url = "https://ezov.mzv.sk/e-zov/dateOfVisitDecision.do?siteLanguage="
    connection_attempts = 0

    while connection_attempts < 3:
        try:
            browser.get(base_url)
            # wait for the change book date of visit btn
            # before returning True
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@name="j_username"]'))
            )
            return True
        except Exception as e:
            print(e)
            connection_attempts += 1
            print(f"Error connecting to the {base_url}.")
            print(f"Attempt #{connection_attempts}.")
    return False
