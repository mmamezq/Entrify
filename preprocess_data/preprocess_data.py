import clean_job_details as c
import utils

def preprocess_data(data_path):
    df = utils.open_data(data_path)
    cleaned_df = c.clean_job_details(df.copy())

    return cleaned_df


