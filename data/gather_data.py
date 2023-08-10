from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import urllib.parse
from secrets import li_username, li_pass
from utils import process_job_item, find_next_job, get_next_page
from database import create_job
import time

def extract_li_data(location_list):
    print("Starting process...")
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
    
    for location in location_list:

        parsed_location = urllib.parse.quote(location)

        job_search_url = f"https://www.linkedin.com/jobs/search/?location={parsed_location}&refresh=true"

        driver.get(job_search_url)

        while True:

            # Wait until the page renders completely
            time.sleep(5)

            job_list = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container > li")
            
            for li in job_list:
                driver.execute_script("arguments[0].scrollIntoView()", li)
                time.sleep(2)

                try:
                    li.find_element(By.CSS_SELECTOR, "div")
                except NoSuchElementException:
                    time.sleep(3)

                job_item = process_job_item(driver)
                create_job(job_item)

                if next_job_id := find_next_job(driver, job_item["job_id"]):
                    driver.find_element(By.XPATH, f"//div[@data-job-id='{next_job_id}']").click()
                else:
                    break
            
            if next_page := get_next_page(driver):
                driver.find_element(By.XPATH, f"//button[@aria-label='Page {next_page}']").click()
            else:
                print(f"All pages for {location} processed.")
                break

    driver.quit()

if __name__ == '__main__':
    states =[
        # "Alaska",
        # "Alabama",
        # "Arkansas",
        # "Arizona",
        # "California",
        # "Colorado",
        # "Connecticut",
        # "District of Columbia",
        # "Delaware",
        # "Florida",
        # "Georgia",
        # "Hawaii",
        # "Iowa",
        # "Idaho",
        # "Illinois",
        # "Indiana",
        # "Kansas",
        # "Kentucky",
        # "Louisiana",
        # "Massachusetts",
        # "Maryland",
        # "Maine",
        "Michigan",
        "Minnesota",
        "Missouri",
        "Mississippi",
        "Montana",
        "North Carolina",
        "North Dakota",
        "Nebraska",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "Nevada",
        "New York",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Virginia",
        "Vermont",
        "Washington",
        "Wisconsin",
        "West Virginia",
        "Wyoming"
    ]
    location_list = [f"{state}, United States" for state in states]
    extract_li_data(location_list)