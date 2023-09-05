import spacy

nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

def tokenize(df):
    print('Tokenizing cleaned text...')
    df['tokens'] = df['cleaned_job_details'].apply(tokenize_text)
    return df
