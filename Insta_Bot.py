import selenium.webdriver.common.touch_actions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#define webdriver and emulate IPhone X
PATH = "C:\Program Files (x86)\chromedriver.exe"
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(PATH, options=chrome_options)
driver.get("https://www.instagram.com/")

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.counter  = 0

    def login(self):
        #accept cookies and press login button
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/button[1]")))
        element.click()
        sleep(1)
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]")))
        element.click()
        #type in username and password
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")))
        element.send_keys(self.username)
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input")))
        element.send_keys(self.password)
        #click login button
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button")))
        element.click()
        #press dont safe information button
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/div/div/button")))
        element.click()
        #press dont add instagram to favoruite sides
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
        element.click()
        #scroll down, so the activate notification button appears
        driver.execute_script("window.scrollBy(0,2000)", "")
        #press false on activate notifiation
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
        element.click()
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/section/div[2]/div/div[1]/button/span")))
        element.click()

    def goToStart(self):
        driver.get("https://www.instagram.com/")

    def likeByHashtag(self,hashtags,amount):
        #open instagram site with the tag
        for hashtag in hashtags:
            driver.implicitly_wait(60)
            driver.get('https://www.instagram.com/explore/tags/' + hashtag)
            for i in range(0,amount+1):
                # find all pictures and put into list
                elements = driver.find_elements_by_class_name("_9AhH0")
                #take one element out of list
                element = elements[i]
                #open it
                element.click()
                element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div/article/div[3]/section[1]/span[1]/button/div/span")))
                element.click()
                sleep(6)
                #go back
                driver.back()

    def upload(self, image, text):
        driver.get("https://www.instagram.com/")
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]"))).click()
        #find input field
        upload_btn = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        time.sleep(2)
        #send image
        upload_btn.send_keys("C:\\Users\\brend\PycharmProjects\ClimateCoinBot\\PP2.jpg") #full path of the file which is to be uploaded

acc = Instagram("climatecoinbot", "Arne2005")
acc.login()
acc.upload()
#rn.likeByHashtag(["hello"],10)
sleep(120)

#quit
driver.quit()
driver.close()