import json
import pandas as pd


def create_dataset(data_path):
    f = open(data_path)
    data = json.load(f)
    main_key = [key for key in data.keys() if isinstance(key, str)][0]
    jobs_dict = data[main_key]['jobs']
    df = pd.DataFrame.from_dict(jobs_dict, orient='index')
    df = df.drop(columns=['__collections__'])
    df.reset_index(drop=True, inplace=True)
    return df