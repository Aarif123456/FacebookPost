from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random

def post(driver, targetUrl: str, message: str):
    driver.get(targetUrl)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span"))).click()
    sleep(3)
    closeButton = driver.find_element_by_xpath("//*[@aria-label='Close']");
    
    for line in message.split("\n"):
        miniAction = ActionChains(driver)
        print(line)
        miniAction.send_keys(line)
        miniAction.send_keys(Keys.ENTER)
        miniAction.perform()
        sleep(random.uniform(0.2, 0.5))

    actions = ActionChains(driver) ##Action Chains 
    actions.send_keys(Keys.TAB *9)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print ("Posted...")

