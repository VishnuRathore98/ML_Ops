from transformers import AutoTokenizer
import torch
from datasets import load_from_disk
from pprint import pprint
import os

device = torch.device('cuda')
dataset_path = './local_datasets/imdb_labeled'
tokenized_dataset_path = './local_datasets/imdb_tokenized'
model_checkpoint = 'huawei-noah/TinyBERT_General_4L_312D'

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

def tokenize(batch):
    temp = tokenizer(batch['review'], padding=True, truncation=True, max_length=300)
    return temp

dataset = load_from_disk(dataset_path)

tokenized_dataset = dataset.map(tokenize, batched=True, batch_size=None)

if not os.path.exists(tokenized_dataset_path):
    os.makedirs(tokenized_dataset_path)

tokenized_dataset.save_to_disk(tokenized_dataset_path)

print(f'Tokenized dataset saved to: {tokenized_dataset_path}')

pprint(tokenized_dataset['train'][0].keys())
