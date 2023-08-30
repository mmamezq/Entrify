import re
from autocorrect import Speller

def remove_text_markup(text):
    clean_text = re.sub(r'<.*?>', '', text) # Remove any HTML markup
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

def remove_bullet_points(text):
    # Replace bullet points (• or * followed by space) with an empty string
    cleaned_text = re.sub(r'•\s*|\*\s*', '', text)

    # Remove leading hyphens followed by space, but preserve other hyphens
    cleaned_text = re.sub(r'^(?=-\s)', '', cleaned_text, flags=re.MULTILINE)

    # Remove multiple hyphens ex: ------
    cleaned_text = re.sub(r'-{2,}', '', cleaned_text)
    return cleaned_text

def remove_extra_punctuation(text):
    cleaned_text = re.sub(r"[.]{2,3}", '', text)
    cleaned_text = re.sub(r"[_]{2,}", '', text)
    return cleaned_text

def remove_inclusion_statement(text):
    cleaned_text = re.sub(r'we (do not|don\'t | prohibit) (discriminate | discrimination) ?(.*) based ?(on|upon) .*?', '', text)
    return cleaned_text

def remove_email_address(text):
    cleaned_text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'EMAIL',text)
    return cleaned_text
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

    # Remove bullet points
    print('Removing bullet points')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_bullet_points)

    # Correct any typos
    print('Correcting typos...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(autocorrect_typos)

    # Remove additional punctuation (ellipsis ...)
    print('Removing additional punctuation...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_extra_punctuation)

    # Remove inclusion statement
    print('Removing inclusion statements...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_inclusion_statement)

    # Remove additional punctuation (ellipsis ...)
    print('Removing email addresses...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_email_address)

    return df