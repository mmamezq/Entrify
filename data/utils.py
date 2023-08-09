from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def process_job_item(driver):
    job_item = {}

    li_levels = {
        "Internship": 0,
        "Entry level": 1,
        "Associate": 2,
        "Mid-Senior level": 3,
        "Director": 4,
        "Executive": 5
    }

    html = soupify(driver)
    url = driver.current_url
    parsed_url = urlparse(url)

    try:
        # Get job ID from the URL query parameter
        job_item["job_id"] = parse_qs(parsed_url.query).get("currentJobId", None)[0]
        # Company name -> child of div class "jobs-unified-top-card__primary-description" > div > a
        job_item["company_name"] = html.css.select(".jobs-unified-top-card__primary-description a")[0].get_text().strip()\
            if html.css.select(".jobs-unified-top-card__primary-description a") else None
        # LinkedIn job level category -> child of li class "jobs-unified-top-card__job-insight" > span > after center dot e.g. ("Full-time · Mid-Senior level")
        job_item["li_level"] = li_levels.get(html.css.select(".jobs-unified-top-card__job-insight > span")[0].get_text().split("· ")[-1].strip()) \
            if html.css.select(".jobs-unified-top-card__job-insight > span") else None
        # Job title -> h2 class "jobs-unified-top-card__job-title"
        job_item["job_title"] = html.css.select(".jobs-unified-top-card__job-title")[0].get_text().strip()
        # String only version 
        job_item["job_details"] = html.find("div", id = "job-details").get_text(" ")

    except:
        raise ValueError("There was an error when finding job information."
                         + " This may be due to a login issue (e.g. a security challenge)"
                         + " or a change in the HTML format."
                         + " Please investigate the issue.")
    return job_item


def soupify(driver):
    src = driver.page_source
    return BeautifulSoup(src, 'html.parser')


def extract_job_list(driver):
    html = soupify(driver)
    return html.css.select(".scaffold-layout__list-container > li")


def find_next_job(driver, job_id):
    html = soupify(driver)
    origin = html.find("div", {"data-job-id": job_id})
    next_job = origin.find_next("div", class_ = "job-card-container--clickable")
    
    return next_job["data-job-id"] if next_job else None


def get_next_page(driver):
    html = soupify(driver)
    page_info = html.css.select(".artdeco-pagination__page-state")[0].get_text().split()
    current_page = page_info[1]
    max_page = page_info[-1]

    return None if current_page == max_page else str(int(current_page) + 1)