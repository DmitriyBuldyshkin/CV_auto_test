from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

address = "https://job.mts.ru/programs/start/521648931474506519"
button1 = "Хочу на стажировку в МТС"
data = {
    
}

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 2 
})
driver = webdriver.Chrome(options=options)

driver.get(address)
wait = WebDriverWait(driver, 15)

elem = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(., '{button1}')]")))
driver.execute_script("arguments[0].scrollIntoView(true);", elem)
elem.click()

div_label = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']")))
driver.execute_script("arguments[0].scrollIntoView(true);", div_label)
div = div_label.find_element(By.XPATH, '..')
name = div.find_element(By.XPATH, '//input')
name.send_keys("Дмитрий")

time.sleep(15)
driver.quit()