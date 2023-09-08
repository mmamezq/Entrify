import torch
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


def tokenize_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens

def tokenize(df):
    print('Tokenizing cleaned text...')
    df['tokens'] = df['cleaned_job_details'].apply(tokenize_text)
    return df
