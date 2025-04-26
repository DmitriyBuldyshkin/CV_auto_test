from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 2 
})
driver = webdriver.Chrome(options=options)

driver.get('https://job.mts.ru/programs/start/521648931474506519')
wait = WebDriverWait(driver, 15)

elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Хочу на стажировку в МТС')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", elem)
elem.click()

time.sleep(15)
driver.quit()