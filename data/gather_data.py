from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from secrets import li_username, li_pass
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

# Wait until the page renders completely
time.sleep(10)

username = driver.find_element(By.ID, "username")
username.send_keys(li_username)

pword = driver.find_element(By.ID, "password")
pword.send_keys(li_pass)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

job_search_url = "https://www.linkedin.com/jobs/search/?location=United%20States&refresh=true"

driver.get(job_search_url)

# Wait until the page renders completely
time.sleep(10)