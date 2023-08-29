import pandas as pd
import re
import json
from autocorrect import Speller

def open_data(data_path):
    f = open(data_path)
    data = json.load(f)
    main_key = [key for key in data.keys() if isinstance(key, str)][0]
    jobs_dict = data[main_key]['jobs']
    df = pd.DataFrame.from_dict(jobs_dict, orient='index')
    df = df.drop(columns=['__collections__'])
    df.reset_index(drop=True, inplace=True)
    return df

def remove_text_markup(text):
    clean_text = re.sub(r'<.*?>', '', text)
    clean_text = re.sub(r'\n+', '', clean_text) # Replace newline character
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Replace multiple spaces with a single space
    clean_text = re.sub(r'About the job', '', clean_text, flags=re.IGNORECASE)  # Remove 'About the job'

    return clean_text

def autocorrect_typos(text):
    spell = Speller(lang='en')
    clean_text = spell(text)
    return clean_text

def lowercase_text(text):
    lowercase_text = str.lower(text)
    return lowercase_text

def remove_privateuse_chars(text):
    clean_text = text.replace('\uf0b7', '')
    return clean_text

def clean_job_details(df):
    # Remove any text markup from LinkedIn
    print('Removing text markup...')
    df['cleaned_job_details'] = df['job_details'].apply(remove_text_markup)

    # Lowercase all text
    print('Lowercasing text...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(lowercase_text)

    # Remove private use characters
    print('Removing private use characters...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_privateuse_chars)

    # Correct any typos
    print('Correcting typos...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(autocorrect_typos)

    return df