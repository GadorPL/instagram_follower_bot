from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

CHROME_DRIVER_PATH = "/Development/chromedriver"
SIMILAR_ACCOUNT = "pycoders"   # Account whose followers you'll follow.
INSTA_EMAIL = os.getenv("INSTA_EMAIL")
PASSWORD = os.getenv("PASSWORD")


class InstaFollower:
    def __init__(self):
        self.service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        sleep(3)
        accept_cookies_btn = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        accept_cookies_btn.click()
        sleep(3)
        name_input_insta = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        name_input_insta.send_keys(INSTA_EMAIL)
        sleep(2)
        pass_input_insta = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input_insta.send_keys(PASSWORD)
        sleep(1)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        sleep(10)
        not_now_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()
        sleep(3)
        next_not_now = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        next_not_now.click()
        sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(4)
        followers_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]'
                                                           '/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()
        sleep(3)

    def follow(self):
        scrollbar = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):  # you can make this number bigger for larger accounts.
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollbar)
            sleep(2)
        all_followers = self.driver.find_elements(By.CSS_SELECTOR, ".sqdOP")
        sleep(2)
        for follower in all_followers:
            try:
                follower.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
                sleep(1)
        sleep(7)
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
