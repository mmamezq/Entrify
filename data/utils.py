from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def process_job_item(driver):
    job_item = {}

    src = driver.page_source
    html = BeautifulSoup(src, 'html.parser')
    url = driver.current_url
    parsed_url = urlparse(url)
    # Get job ID from the URL query parameter

    try:
        job_item["job_id"] = parse_qs(parsed_url.query).get("currentJobId", None)[0]
        # Company name -> child of div class "jobs-unified-top-card__primary-description" > div > a
        job_item["company_name"] = html.css.select(".jobs-unified-top-card__primary-description a")[0].get_text().strip()
        # LinkedIn job level category -> child of li class "jobs-unified-top-card__job-insight" > span > after center dot e.g. ("Full-time · Mid-Senior level")
        job_item["li_level"] = html.css.select(".jobs-unified-top-card__job-insight > span")[0].get_text().split("· ")[1].strip()
        # Job title -> h2 class "jobs-unified-top-card__job-title"
        job_item["job_title"] = html.css.select(".jobs-unified-top-card__job-title")[0].get_text().strip()
        # Job description -> div id = "job-details"
        job_item["job_details_html"] = html.find("div", id = "job-details")
        # String only version 
        job_item["job_details_string"] = job_item["job_details_html"].get_text(" ")

    except:
        raise ValueError("There was an error when finding job information."
                         + " This may be due to a login issue (e.g. a security challenge)"
                         + " or a change in the HTML format."
                         + " Please investigate the issue.")
    return job_item