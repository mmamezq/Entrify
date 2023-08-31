import clean_job_details as c
import utils


def preprocess_data(data_path, testing=False, num_samples=1000):
    df = utils.open_data(data_path)
    if testing:
        df = df.sample(n=num_samples, random_state=42)
    cleaned_df = c.clean_job_details(df.copy())

    return cleaned_df, 0, 0
