from transformers import BertTokenizer, BertModel
from tensorflow.keras.utils import pad_sequences

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

def tokenize_text(text):
    tokenized_output = tokenizer(text)
    tokens = tokenized_output['input_ids']
    return tokenized_output, tokens

def compute_length(df):
    df['sequence_length'] = df['token_ids'].apply(len)
    percentile_95_length = df['sequence_length'].quantile(0.95)
    return percentile_95_length

def pad_text_sequences(seq, max_length):
    padded_sequence = pad_sequences(seq, maxlen = max_length, padding = 'post', truncating = 'post')
    return padded_sequence

def vectorize(df):
    print('Tokenizing cleaned text...')
    tokenized_ouput, tokens = df['cleaned_job_details'].apply(tokenize_text)
    df['bert_tokenizer_data'] = tokenized_ouput
    max_length = compute_length(df['token_ids'])
    df['token_ids'] = df.apply(lambda row: pad_text_sequences(row['token_ids'], max_length=max_length))


    return df
