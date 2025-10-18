from datasets import Dataset
from pprint import pprint
import pandas as pd
import os

dataset_url = 'https://raw.githubusercontent.com/laxmimerit/All-CSV-ML-Data-Files-Download/master/twitter_disaster_tweets.csv'
local_dataset_path = './local_datasets/twitter_disaster_tweets.csv'
save_to_disk_path = './local_datasets/twitter_disaster_tweets_labled/'


# Storing dataset locally such that data loading time could be decreased
# Checking if dataset exists locally
if not os.path.exists(save_to_disk_path):
    print('Downloading dataset...')
    # Read the dataset from online url to memory
    df = pd.read_csv(dataset_url, usecols=['text','target'])
    # Shuffle the dataset
    df = df.sample(frac=1).reset_index(drop=True)

    os.makedirs(save_to_disk_path)
    # Save the csv file locally without indexing it
    df.to_csv(local_dataset_path, index=False)
else:
    print('Loading cached data...')
    # Reading using pandas does not cache in memory for faster access in subsequest accesses 
    df = pd.read_csv(local_dataset_path)

    # Shuffle the dataset
    df = df.sample(frac=1).reset_index(drop=True)

# Get max text string length
max_len = max(df['text'].str.len())

# rename target col to label as it is required for tinyBERT model
df = df.rename(columns={'target':'label'})

# Convert pandas df to HF dataset
dataset = Dataset.from_pandas(df)

# split dataset into train and test splits
dataset = dataset.train_test_split(test_size=0.2)

dataset.save_to_disk(save_to_disk_path)

print("Labeled dataset saved.")
