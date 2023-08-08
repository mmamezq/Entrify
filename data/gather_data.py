from selenium import webdriver
from selenium.webdriver.common.by import By
from secrets import li_username, li_pass
from utils import process_job_item, extract_job_list, find_next_job
import time

def extract_li_data():
    # for testing
    all_jobs = []
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")

    # Wait until the page renders completely
    time.sleep(5)

    username = driver.find_element(By.ID, "username")
    username.send_keys(li_username)

    pword = driver.find_element(By.ID, "password")
    pword.send_keys(li_pass)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    if "challenge" in driver.current_url:
        time.sleep(30)

    if "challenge" in driver.current_url:
        raise Exception("There is a security challenge that selenium can't bypass.")

    job_search_url = "https://www.linkedin.com/jobs/search/?location=United%20States&refresh=true"

    driver.get(job_search_url)

    # Wait until the page renders completely
    time.sleep(5)

    # The next section should loop over each job item in the page. The job items are a li with data-occludable-job-id or a normal html id with "ember" + three digit integer.
    # Possible strategy:
        # for each li in specific div (check id), execute. Once all are done, change the page and redo the whole process
        # I would need to identify the "endpoint" for all search results.
    
    # I need to scroll through the job list at page render to load all of the jobs.
    
    job_list = extract_job_list(driver)

    for li in job_list:
        job_item = process_job_item(driver)
        all_jobs.append(job_item)
        next_job_id = find_next_job(driver, job_item["job_id"])
        driver.find_element(By.XPATH, f"//div[@data-job-id='{next_job_id}']").click()
        time.sleep(2)

    driver.quit()

if __name__ == '__main__':
    extract_li_data()