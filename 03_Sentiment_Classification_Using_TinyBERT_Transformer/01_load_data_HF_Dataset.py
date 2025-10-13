import pandas as pd
from datasets import Dataset, load_dataset
from pprint import pprint
import os
import time


url = 'https://raw.githubusercontent.com/laxmimerit/All-CSV-ML-Data-Files-Download/master/IMDB-Dataset.csv'
local_dataset_path = './local_datasets/IMDB-Dataset.csv'
save_to_disk_path = './local_datasets/imdb_labeled/'

start = time.time()

# Storing dataset locally such that data loading time could be decreased
# Checking if dataset exists locally
if not os.path.exists(save_to_disk_path):
    print('Downloading dataset...')
    # Read the dataset from online url to memory
    data = pd.read_csv(url)
    os.makedirs(save_to_disk_path)
    # Save the csv file locally without indexing it
    data.to_csv(local_dataset_path, index=False)
else:
    print('Loading cached data...')
    # Reading using pandas does not cache in memory for faster access in subsequest accesses 
    #data = pd.read_csv(local_dataset_path)
    # Using dataset's load_dataset function for chaching and quick access 

dataset = load_dataset('csv', data_files=local_dataset_path)

# Fetch the default trainig set 
train_dataset = dataset['train']
# Dividing into training and testing sets 
dataset = train_dataset.train_test_split(test_size=0.3)
# Reading as pandas dataframe
data = pd.read_csv(local_dataset_path)
end = time.time()

# Labeling the data 
label2id = {'positive':1, 'negative':0}
id2label = {1:'positive', 0:'negative'}

# Using the map function to label the data in dataset 
dataset = dataset.map(lambda x: {'label': label2id[x['sentiment']]})

print(f'Time took for data loading and labeling : {end-start:.2f} seconds.')

pprint(dataset['test'][0])

dataset.save_to_disk(save_to_disk_path)

print("Labeled dataset saved.")
