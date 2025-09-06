from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # tryb bez interfejsu
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://www.azair.eu/")

time.sleep(5)

airlines_element = driver.find_element(By.ID, "airlinesList")
airlines = airlines_element.text.split('\n')

df = pd.DataFrame(airlines, columns=["Linia lotnicza"])
df.to_excel("linie_lotnicze_azair.xlsx", index=False)

driver.quit()
