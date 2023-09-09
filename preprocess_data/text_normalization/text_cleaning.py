import re
from autocorrect import Speller
from tqdm import tqdm


def remove_text_markup(text):
    clean_text = re.sub(r'<.*?>', '', text)  # Remove any HTML markup
    clean_text = re.sub(r'\n+', '', clean_text)  # Replace newline character
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Replace multiple spaces with a single space
    clean_text = re.sub(r'About the job', '', clean_text, flags=re.IGNORECASE)  # Remove 'About the job'

    return clean_text

def autocorrect_typos(texts):
    spell = Speller(lang='en')
    corrected_texts = []
    print(texts)
    for text in tqdm(texts, desc="Processing texts"):
        clean_text = spell(text)
        corrected_texts.append(clean_text)

    return corrected_texts


def lowercase_text(text):
    lowercase_text = str.lower(text)

    return lowercase_text


def remove_privateuse_chars(text):
    clean_text = text.replace('\uf0b7', '')

    return clean_text


def remove_bullet_points(text):
    # Replace bullet points (• or * followed by space) with an empty string
    cleaned_text = re.sub(r'•\s*|\*\s* |∙|•', '', text)

    # Remove leading hyphens followed by space, but preserve other hyphens
    cleaned_text = re.sub(r'^(?=-\s)', '', cleaned_text, flags=re.MULTILINE)

    # Remove multiple hyphens ex: ------
    cleaned_text = re.sub(r'-{2,}', '', cleaned_text)
    return cleaned_text


def remove_extra_punctuation(text):
    cleaned_text = re.sub(r"[.]{2,3}", '', text)
    cleaned_text = re.sub(r"[_]{2,}", '', cleaned_text)
    return cleaned_text


def remove_inclusion_statement(text):
    cleaned_text = re.sub(
        r'we (do not|don\'t | prohibit) (discriminate | discrimination) ?(.*) ?(based) ?(on|upon) .*?', '', text)
    return cleaned_text


def remove_email_address(text):
    cleaned_text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'EMAIL', text)
    return cleaned_text


def remove_urls(text):
    url_pattern = re.compile(r'(?:http[s]?://)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|'
                             r'check us out on|visit our website|learn more at | follow us at | follow us on | add us on |'
                             r'email us at | email at | visit',
                             flags=re.IGNORECASE)

    cleaned_text = re.sub(url_pattern, '', text)

    return cleaned_text

def remove_punctuation(text):
    # Use regular expression to match and replace punctuation with spaces
    cleaned_text = re.sub(r'(?<=[^\w\s\.\-])|(?=[^\w\s\.\-])', ' ', text)
    return cleaned_text


def expand_contractions(text):
    contractions_dict = {
        "ain't": "are not",
        "aren't": "are not",
        "can't": "cannot",
        "couldn't": "could not",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hasn't": "has not",
        "haven't": "have not",
        "he's": "he is",
        "how'd": "how did",
        "how'll": "how will",
        "how's": "how is",
        "I'd": "I would",
        "I'll": "I will",
        "I'm": "I am",
        "I've": "I have",
        "isn't": "is not",
        "it's": "it is",
        "let's": "let us",
        "mustn't": "must not",
        "shan't": "shall not",
        "she'd": "she would",
        "she'll": "she will",
        "she's": "she is",
        "shouldn't": "should not",
        "that's": "that is",
        "there's": "there is",
        "they'd": "they would",
        "they'll": "they will",
        "they're": "they are",
        "they've": "they have",
        "we'd": "we would",
        "we'll": "we will",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "where's": "where is",
        "who'd": "who would",
        "who'll": "who will",
        "who're": "who are",
        "who's": "who is",
        "who've": "who have",
        "won't": "will not",
        "wouldn't": "would not",
        "you'd": "you would",
        "you'll": "you will",
        "you're": "you are",
        "you've": "you have",
    }

    for contraction, expansion in contractions_dict.items():
        text = text.replace(contraction, expansion)
    return text

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

    # Remove additional punctuation (ellipsis ...)
    print('Removing additional punctuation...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_extra_punctuation)

    # Removing email addresses...
    print('Removing email addresses...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_email_address)

    # Removing URLs...
    print('Removing URLs...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_urls)

    # Removing punctuations
    print('Removing punctuations...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_punctuation)

    print("Expanding contractions...")
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(expand_contractions)

    print('Correcting typos...')
    df['cleaned_job_details'] = autocorrect_typos(df['cleaned_job_details'])

    # Remove inclusion statement
    print('Removing inclusion statements...')
    df['cleaned_job_details'] = df['cleaned_job_details'].apply(remove_inclusion_statement)

    return df
