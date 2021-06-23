from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

path_to_chromdriver = 'C:/Users/Innocent Suta/chromedriver.exe' #Make sure to save the chromedriver.xe to your root path

driver = webdriver.Chrome(path_to_chromdriver)

driver.get("https://website.com/login") #Login in link

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-username-input"]'))) #username field XPATH. 
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-password-input"]'))) #Xpath for login field.. Note: you can use any selector

username.clear()
username.send_keys("Your username/email")

password.clear()
password.send_keys("Your Password")
 
Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="login-submit-button"]'))).click() #xpath for submit button