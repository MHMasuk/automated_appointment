import datetime
import sys
import requests
from time import sleep, time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

        # ok_btn = browser.find_element(By.XPATH, "//*[@class='pointer']")
        # ok_btn.click()
        # # sleep(2)
        #
        #
        # make_reservation_btn = browser.find_element(By.XPATH, '//*[@class="infoTable"]//tr//td//a')
        # make_reservation_btn.click()
        # # sleep(2)
        #
        # select = Select(browser.find_element(By.XPATH, '//select[@id="calendar.consularPost.consularPost"]'))
        # select.select_by_visible_text("Baku")
        # ok_btn = browser.find_element(By.XPATH, "//font[text()='OK']")
        # ok_btn.click()
        # # sleep(2)
        #
        # date_click = browser.find_elements(By.XPATH, '//*[@class="calendarMonthCell"]//strong')[1]
        # date_click.click()
        # # sleep(2)
        #
        # slot_click = browser.find_elements(By.XPATH, '//*[@class="calendarDayTableRow"]')[1]
        # slot_click.click()
        # sleep(6)
        #
        # Extract the cookies from the browser
        cookies = browser.get_cookies()

        # Create a session
        session = requests.session()

        # Add the cookies to the session
        for cookie in cookies:
            session.cookies.update({cookie['name']: cookie['value']})

        print("cookies", cookies)
        print("session", session)

        # https://ezov.mzv.sk/e-zov/calendarDay.do?day=19.01.2023&timeSlotId=&calendarId=&consularPostId=1070
        # calendar.timeOfVisit:
        # 19.01
        # .2023
        # 10: 00
        # calendar.sequenceNo:
        # 1
        # calendar.timeSlot.timeSlotId:
        # calendar.consularPost.consularPost:
        # 1070
        # calendar.calendarId:
        # captcha:
        # 82
        # ckh

        # The URL to send the POST request to
        url = 'https://ezov.mzv.sk/e-zov/calendarDay.do?day=19.01.2023&timeSlotId=&calendarId=&consularPostId=1070'

        # The data to include in the POST request
        data = {
            'calendar.timeOfVisit': '19.01.2023 10:00',
            'calendar.sequenceNo': '1',
            'calendar.timeSlot.timeSlotId': None,
            'calendar.consularPost.consularPost': 1070,
            'calendar.calendarId:': None,
            'captcha': "82ckh"
        }

        # Send the POST request
        response = session.post(url, json=data)
        # response = session.get(url)

        # Print the response
        print(response.text)
        # captcha_input = browser.find_element(By.XPATH, '//*[@id="captcha"]')
        # captcha_input.send_keys("2ydrw")
        # sleep(2)

        captcha_input = browser.find_elements(By.XPATH, '//*[@class="pointer"]')[7]
        print(captcha_input.text)
        captcha_input.click()
        sleep(8)



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
