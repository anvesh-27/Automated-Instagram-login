from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

try:
    with open("Creds.txt", "r") as f:
        Username,Password = f.readlines()
except:
    username = str(input("Username: "))
    passwd = str(input("Password: "))
    f = open("Creds.txt", "w")
    f.write(f"{username}\n")
    f.write(f"{passwd}")
    f.close
    
    f = open("Creds.txt", "r")
    Username,Password = f.readlines()

options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

PATH = f"{os.getcwd()}/chromedriver.exe"
driver = webdriver.Chrome(chrome_options = options , executable_path=PATH)
CREDS =  {"username":f"{Username}","passwd":f"{Password}"}

def login():

    usernamefield = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    usernamefield.click()
    usernamefield.send_keys(CREDS['username'])
    time.sleep(2)

    passfield = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    passfield.click()
    passfield.send_keys(CREDS["passwd"])

    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click()

def startbrowser():

    driver.get("https://www.instagram.com/?hl=en")
    time.sleep(5)
    login()

startbrowser()