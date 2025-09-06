from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Konfiguracja Chrome w trybie headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Uruchomienie WebDrivera
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.azair.eu/")

# Czekamy na załadowanie strony
time.sleep(5)

# Pobieramy listę linii lotniczych
try:
    airlines_element = driver.find_element(By.ID, "airlinesList")
    airlines = airlines_element.text.split('\n')
except Exception as e:
    airlines = ["Błąd podczas pobierania danych:", str(e)]

# Tworzymy DataFrame
df = pd.DataFrame(airlines, columns=["Linia lotnicza"])

# Zapis do Excela
df.to_excel("linie_lotnicze_azair.xlsx", index=False)

# Zamykanie przeglądarki
driver.quit()
