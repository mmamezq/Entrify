import preprocess_data as ppd

def main(data_path):
    cleaned_df, tokens, vocabulary = ppd.preprocess_data(data_path)

    return cleaned_df, tokens, vocabulary

if __name__ == '__main__':
    data_path = 'data_081723.json'
    cleaned_df, tokens, vocabulary = main(data_path)

    print("Cleaned DataFrame:", cleaned_df)
    print("Tokens:", tokens)
    print("Vocabulary:", vocabulary)

