import datetime
import sys
from time import sleep, time

from selenium.webdriver.common.by import By
from scrapers.scraper import connect_to_base, get_driver


def run_process(browser):
    if (connect_to_base(browser)):
        sleep(2)
        print("browser", browser)

        # change_book_date_btn = browser.find_element(By.XPATH, '//div[@id="menuArea"]//span[2]')
        # change_book_date_btn.click()
        # sleep(10)

        username_input = browser.find_element(By.XPATH, '//table[@class="infoTable"]//input[@id="j_username"]')
        password_input = browser.find_element(By.XPATH, "//input[@id='j_password']")
        username_input.send_keys("uhuuewhuuos")
        password_input.send_keys("B00078734")
        sleep(2)

        ok_btn = browser.find_element(By.XPATH, "//*[@class='pointer']")
        ok_btn.click()
        sleep(2)

        sleep(5)

        make_reservation_btn = browser.find_element(By.XPATH, '//*[@class="infoTable"]//tr//td//a')
        make_reservation_btn.click()



    else:
        print("Failed to connect to the site")


if __name__ == "__main__":

    # headless mode?
    headless = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "headless":
            print("Running in headless mode")
            headless = True

    # set variables
    start_time = time()

    # init browser
    browser = get_driver(headless=headless)

    # automated script
    print(f"Automated process is starting....")
    run_process(browser)

    # exit
    browser.quit()
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed run time: {elapsed_time} seconds.")
