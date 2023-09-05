import text_cleaning as c
import tokenizer as t
import utils


def preprocess_data(data_path, testing=False, num_samples=1000):
    df = utils.open_data(data_path)
    if testing:
        df = df.sample(n=num_samples, random_state=42)
    cleaned_df = c.clean_job_details(df.copy())
    tokenized_df = t.tokenize(cleaned_df.copy())
    return tokenized_df, 0, 0
