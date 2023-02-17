from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://randomwordgenerator.com/paragraph.php") #Browser goes to website

content = driver.find_element(By.CLASS_NAME, "support-paragraph")


with open('madlib_websource.txt', 'w') as web:
    web.write(content.text)