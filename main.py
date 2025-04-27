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

dropdown = {
    "Год выпуска": 2023,
    "Уровень": "Бакалавриат"
}

text = "Заинтересовала данная вакансия, есть опыт в ручном тестировании, немного умею писать автотесты, в качестве доказательства написал скрипт, который сделал отклик на эту вакансию за меня, с кодом можете ознакомиться здесь: "

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

def drop_down(key, value):
    drop = driver.find_element(By.XPATH, f"//label[text()='{key}']")
    div = drop.find_element(By.XPATH, '../..')
    span = div.find_element(By.TAG_NAME, 'span')
    span.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='autocomplete-list']//li")))
    var = driver.find_element(By.XPATH, f"//ul[@class='autocomplete-list']//li//span[text()='{value}']")
    var.click()

button_click(button1)

for key, value in personal_data.items():
    data_insert(key, value)

wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='autocomplete-list']//li")))
c_list = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-list']//li")
c_list[2].click()

for key, value in education.items():
    data_insert(key, value)

for key, value in dropdown.items():
    drop_down(key, value)

file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys("/Users/dmitriy/Downloads/Тестировщик.pdf")

text_area = driver.find_element(By.TAG_NAME, 'textarea')
text_area.send_keys(text)

check = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
driver.execute_script("arguments[0].click();", check)

button_click(button2)

time.sleep(10)
driver.quit()