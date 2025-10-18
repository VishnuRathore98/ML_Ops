from transformers import AutoTokenizer
from datasets import load_from_disk
from pprint import pprint
import torch
import os

model_checkpoint = 'huawei-noah/TinyBERT_General_4L_312D'
dataset_path = './local_datasets/twitter_disaster_tweets_labled/'
tokenized_dataset_path = './local_datasets/twitter_disaster_tweets_tokenized/'

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

def tokenize(batch):
  temp = tokenizer(batch['text'], padding=True, truncation=True, max_length=100)
  return temp

dataset = load_from_disk(dataset_path)

tokenized_dataset = dataset.map(tokenize, batched=True, batch_size=None)

if not os.path.exists(tokenized_dataset_path):
    os.makedirs(tokenized_dataset_path)

tokenized_dataset.save_to_disk(tokenized_dataset_path)

print(f"Tokenized dataset saved to:{tokenized_dataset_path}")

pprint(tokenized_dataset['train'][0].keys())
