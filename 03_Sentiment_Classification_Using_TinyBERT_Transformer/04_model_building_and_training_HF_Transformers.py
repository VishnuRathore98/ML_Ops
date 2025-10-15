from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments, AutoTokenizer
import evaluate 
import numpy as np
from datasets import load_from_disk

tokenized_dataset_path = './local_datasets/imdb_tokenized'

model_checkpoint = 'huawei-noah/TinyBERT_General_4L_312D'

# Labels
label2id = {'positive':1, 'negative':0}
id2label = {1:'positive', 0:'negative'}

# For evaluation 
accuracy = evaluate.load('accuracy')

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)

# Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)
print("-----------tokenizer initialized-------------")

#Dataset
tokenized_dataset=load_from_disk(tokenized_dataset_path)
print("------------tokenized dataset loaded---------")

model = AutoModelForSequenceClassification.from_pretrained(
                            model_checkpoint,
                            num_labels=len(label2id),
                            label2id = label2id,
                            id2label= id2label
                            )

print("-------------model initialized----------------")

args = TrainingArguments(
    output_dir='train_dir',
    overwrite_output_dir=True,
    num_train_epochs=3,
    learning_rate=2e-5,
    per_device_eval_batch_size=32,
    per_device_train_batch_size=32,
    eval_strategy='epoch',
    #This will make training extremely slow
    #no_cuda=True
)

print("----------training arguments set---------------- ")

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test'],
    compute_metrics=compute_metrics,
    tokenizer=tokenizer
)

print("-----------trainer initialized:------------------- ")

trainer.train()

print("----------- model training completed------------------")
trainer.evaluate()

print("-----------model evaluation completed------------------")
