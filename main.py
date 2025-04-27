from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

address = "https://job.mts.ru/programs/start/521648931474506519"
button1 = "Хочу на стажировку в МТС"
button2 = "Подать заявку"

personal_data = {
    "Имя": "Дмитрий",
    "Фамилия": "Булдышкин",
    "Телефон": 9173765880,
    "Почта": "BuldyshkinDmitriy@yandex.ru",
    "Город": "Москва"
}

education = {
    "ВУЗ": "Уфимский университет науки и технологий",
    "Специальность": "Автоматизация технологических процессов и производств"
}

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 2 
})
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

driver.get(address)

def button_click(button):
    elem = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(., '{button}')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", elem)
    elem.click()

def data_insert(key, value):
    div_label = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[text()='{key}']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", div_label)
    div = div_label.find_element(By.XPATH, '../..')
    name = div.find_element(By.XPATH, './/input')
    name.send_keys(value)

button_click(button1)

for key, value in personal_data.items():
    data_insert(key, value)

wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='autocomplete-list']//li")))
c_list = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-list']//li")
c_list[2].click()

for key, value in education.items():
    data_insert(key, value)

time.sleep(15)
driver.quit()