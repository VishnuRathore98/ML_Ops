import datasets
import os

dataset_url = "Bingsu/Human_Action_Recognition"

local_dataset_path = './local_datasets/human_action_dataset'
save_to_disk_path = './local_datasets/human_action_dataset_labled/'

# Storing dataset locally such that data loading time could be decreased
# Checking if dataset exists locally
if not os.path.exists(save_to_disk_path):
    print('Downloading dataset...')
    # Read the dataset from online url to memory
    
    data = datasets.load_dataset(dataset_url, split='train')

    data = data.shuffle().train_test_split(test_size=0.2)
    labels = data['train'].features['labels'].names

    label2id, id2label = dict(), dict()

    for i, label in enumerate(labels):
      label2id[label] = i
      id2label[i] = label

    os.makedirs(save_to_disk_path)
    
    data.save_to_disk(save_to_disk_path)

print("Labeled dataset saved.")
