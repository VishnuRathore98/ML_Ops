from transformers import pipeline
import torch

model = 'TinyBERT-sentiment-analysis'

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

classifier = pipeline('text-classification', model=model, device=device)

data=["This movie was absolutely fantastic! The acting was superb and the story was engaging.",
    "I was really disappointed with this film. The plot was predictable and the characters were bland.",
    "An average movie, not great but not terrible either. It had some good moments but overall it was just okay.",
    "The best movie I've seen in a long time! Highly recommended.",
    "I couldn't even finish watching this. It was so boring.",
    "The special effects were amazing, but the story was weak."]

classifier(data)
