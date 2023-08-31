from importlib import reload
import textwrap

import preprocess_data as ppd

reload(ppd)


def main(data_path, testing=False, num_samples=100):
    cleaned_df, tokens, vocabulary = ppd.preprocess_data(data_path, testing, num_samples=100)

    return cleaned_df, tokens, vocabulary


if __name__ == '__main__':
    data_path = 'backup.json'
    cleaned_df, tokens, vocabulary = main(data_path, testing=True, num_samples=100)

    wrap_width = 80
    while True:
        selected_row = cleaned_df.sample(n=1)

        job_details = selected_row['cleaned_job_details'].values[0]
        original_job_deats = selected_row['job_details'].values[0]

        wrapped_job_details = textwrap.fill(job_details, width=wrap_width)
        wrapped_OGjob_details = textwrap.fill(original_job_deats, width=wrap_width)

        print("\nJob Details:")
        print(wrapped_job_details)
        print("\n Original Job Description: ")
        print(wrapped_OGjob_details)

        user_input = input("Press Enter for the next random sample, or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break

    print("Cleaned DataFrame:", cleaned_df)
    print("Tokens:", tokens)
    print("Vocabulary:", vocabulary)
