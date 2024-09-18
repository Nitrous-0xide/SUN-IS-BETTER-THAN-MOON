import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_sun_button(driver):
    try:

        sun_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sun-btn"))
        )

        while True:
            sun_button.click()
            time.sleep(0.01)
    except Exception as e:
        print(f"An error occurred: {e}")

def open_and_click():

    driver = webdriver.Chrome()


    url = "https://neal.fun/sun-vs-moon/"


    driver.get(url)

    try:

        consent_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button"))
        )

        consent_button.click()


        time.sleep(2)


        click_sun_button(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


threads = []
for _ in range(4):
    thread = threading.Thread(target=open_and_click)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
