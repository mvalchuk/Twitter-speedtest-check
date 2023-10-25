import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



TWITER_LOGIN = "YOUR EMAIL"
TWITER_PASSWORD = "YOUR PASSWORD"
TWITTER_USERNAME = "YOUR USERNAME"
YOU_INTERNET_PROVIDER = 'internet provider name'

service = Service(r"C:\chrom_driver\chromedriver.exe")




class InternetSpeedTwitterBot:
    import time

    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0
    def get_internet_speed(self):
        self.driver.get("http://speedtest.net")
        self.go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.time.sleep(10)
        self.go.click()
        self.time.sleep(60)
        self.upspped = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.upspped.text
        self.downspeed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.downspeed.text
        self.down = (f" down: {self.up}")
        self.up = (f" up: {self.down}")




    def tweet_at_provider(self):
        self.driver.get('http://twitter.com')
        self.twitter = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
        self.twitter.click()
        self.time.sleep(3)
        self.login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.login.send_keys(TWITER_LOGIN)
        self.time.sleep(3)
        self.login.send_keys(Keys.ENTER)
        self.time.sleep(3)
        self.name = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        self.name.send_keys(TWITTER_USERNAME)
        self.time.sleep(3)
        self.name.send_keys(Keys.ENTER)
        self.time.sleep(3)
        self.password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.send_keys(TWITER_PASSWORD)
        self.time.sleep(3)
        self.password.send_keys(Keys.ENTER)
        self.time.sleep(10)
        self.tw = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        self.tw.click()
        self.time.sleep(3)
        self.tw.send_keys(f'Hey Xfinity, why is my internet speed {self.down}/{self.up}  when I pay for 400down/10up? ')
        self.time.sleep(5)
        self.button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        self.button.click()
        self.time.sleep(15)
        print("Done")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()






