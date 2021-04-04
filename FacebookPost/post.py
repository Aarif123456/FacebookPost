from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def post(driver, targetUrl: str, message: str):
    driver.get(targetUrl)
    WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']"))).click()
    sleep(3)
    closeButton = driver.find_element_by_xpath("//*[@aria-label='Close']");
    actions= ActionChains(driver) ##Action Chains
    actions.send_keys(message)
    actions.send_keys(Keys.TAB *9)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print ("Posted...")

