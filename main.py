from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
USERNAME = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"
chrome_driver_path = "D://Applications/chromedriver_win32/chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        self.start = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        self.start.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span').text
        print("Download Speed", self.down)
        print("Upload Speed", self.up)

    def tweet_at_provider(self):
        if int(float(self.down)) < PROMISED_DOWN or int(float(self.up)) < PROMISED_UP:
            tweet = f"This is a test message,Hey Internet Provider you said for what i pay, i will receive a minimum " \
                    f"upload speed of {PROMISED_UP}Mbps, download speed of {PROMISED_DOWN}Mbps" \
                    f"but what i receive is {self.up}Mbps and {self.down}Mbps"
            self.driver.maximize_window()
            self.driver.get("https://twitter.com/login?lang=en")
            time.sleep(3)
            login = self.driver.find_element_by_xpath(
                "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
            login.send_keys(USERNAME)
            password = self.driver.find_element_by_xpath(
                "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(2)
            tweet_entry = self.driver.find_element_by_xpath(
                "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div["
                "2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
            tweet_entry.send_keys(tweet)
            time.sleep(1)
            tweet_button = self.driver.find_element_by_xpath(
                "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div["
                "2]/div[3]/div/div/div[2]/div[3]/div")
            tweet_button.click()
        else:
            print("Internet speed is good")


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
