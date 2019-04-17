import onetimepass as otp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import SECRET, EMAIL, PASSWORD
from helpers import get_web_driver

driver = get_web_driver(headless=False)
driver.get('https://gmail.com')
driver.find_element_by_id('identifierId').send_keys(EMAIL)
driver.find_element_by_id('identifierNext').click()
password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="password"]//input'))
    )
password_input.send_keys(PASSWORD)
driver.find_element_by_id('passwordNext').click()
totpPin_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'totpPin'))
    )
totpPin_input.send_keys(otp.get_totp(SECRET))
driver.find_element_by_id('totpNext').click()
