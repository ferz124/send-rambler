from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# создаем объект драйвера Firefox
driver = webdriver.Firefox()

# переходим на страницу для создания нового письма
driver.get("https://mail.rambler.ru/compose")

# находим первое поле для ввода и вводим в него адрес электронной почты
to_field = driver.find_element_by_name("to")
to_field.send_keys("dpopko1982@gmail.com")

# находим второе поле для ввода и вводим в него текст
subject_field = driver.find_element_by_name("subj")
subject_field.send_keys("Hi")

# находим третье поле для ввода и вводим в него текст
body_field = driver.find_element_by_id("tinymce")
body_field.send_keys("No")

# находим кнопку "Отправить" и нажимаем на нее
send_button = driver.find_element_by_xpath("//button[text()='Отправить']")
send_button.click()

# закрываем окно браузера
driver.quit()
