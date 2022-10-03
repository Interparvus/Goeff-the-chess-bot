from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import json
driver = webdriver.Chrome("C:\\Users\\admin\\schecter\\Pracovná plocha\\Goeff the chess bot\\Goeff-the-chess-bot\\chromedriver_win32\\chromedriver.exe")
url = "https://www.chess.com"
driver.get(url)
time.sleep(3)