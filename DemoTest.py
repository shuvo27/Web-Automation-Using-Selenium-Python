from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

# driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://159.89.38.11/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email-1']").send_keys("test@orangetoolz.com")
driver.find_element(By.XPATH, "//input[@id='password-1']").send_keys("8Kh8nTe*^jdk")
driver.find_element(By.XPATH, "//button[@id='m_login_signin_submit']").click()

time.sleep(10)

class MouseOver():
    def mouse_over_events(self):

        button = driver.find_element(By.XPATH,"//div[@class='dt-sidebar__container position-relative']")
        action = ActionChains(driver)
        action.move_to_element(button).perform()

        time.sleep(5)
        driver.find_element(By.XPATH,"//a[@title='Contact Manage']").click()
        time.sleep(5)

        # actions = ActionChains(driver)
        # sidenav = driver.find_element(By.XPATH,"//a[@title='Contact Manage']")
        # actions.move_to_element(sidenav).perform()
mouse = MouseOver()
mouse.mouse_over_events()

addCon = driver.find_element(By.XPATH, "//a[@class='btn btn-shadow btn-info compose-btn add-contact']")
addCon.click()

time.sleep(5)

driver.find_element(By.XPATH, "//input[@type='number']").send_keys("01678888888")
driver.find_element(By.XPATH, "//div[@class='form-div']//input[@type='text']").send_keys("test123@gmail.com")
driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Test")
driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Name")

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()



time.sleep(10)
