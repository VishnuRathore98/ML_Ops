import datasets
from transformers import AutoImageProcessor
from torchvision.transforms import RandomResizedCrop, Compose, Normalize, ToTensor

model_checkpoint = 'google/vit-base-patch16-224-in21k'
dataset_path = './local_datasets/human_action_dataset_labled/'

image_processor = AutoImageProcessor.from_pretrained(model_checkpoint, use_fast=True)

normalize = Normalize(mean=image_processor.image_mean, std=image_processor.image_std)

size = (image_processor.size['shortest_edge'] if 'shortest_edge' in image_processor.size else (image_processor.size['height'], image_processor.size['width']))

_transforms = Compose([RandomResizedCrop(size), ToTensor(), normalize])

def transforms(batch):
  batch['pixel_values'] = [_tansforms(img.convert('RGB')) for img in batch['image']]
  del batch['image']
  return batch

data = datasets.load_from_disk(dataset_path)

dataset = data.with_transform(transforms)
