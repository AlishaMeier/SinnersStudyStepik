from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

# Введем то, что нашли
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

# Кликаем чекбокс и радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()

# Клик на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()