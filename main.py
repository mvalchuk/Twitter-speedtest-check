import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Internet_speedtest_Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.download_speed = 0
        self.upload_speed = 0
        self.xlogin = 'your login'
        self.xpassword = 'your password'
        self.name = 'your name'

    # Getting actual internet speed
    def run_speed_test(self):
        self.driver.get('https://speedtest.xfinity.com/')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div/div/button').click()
        time.sleep(20)
        download_data = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/details/summary/div/dl/dd').text
        # Stored download speed data
        self.download_speed = download_data
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/details/summary/div/div/p').click()
        time.sleep(15)
        upload_data = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/details/div/div/dl/div[1]/dd').text
        # Stored upload speed data
        self.upload_speed = upload_data

    # Login to social media
    def twitter_login(self):
        self.driver.get('https://x.com')
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(self.xlogin)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(self.name)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(self.xpassword)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(f'Hello Xfinity, why my internet speed for download: {self.download_speed} and upload:{self.upload_speed}, instead 400/100 what I am paying for!!!')
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span').click()
        time.sleep(10)
        self.driver.quit()


# Run our Bot
Bot = Internet_speedtest_Bot()
Bot.run_speed_test()
Bot.twitter_login()









