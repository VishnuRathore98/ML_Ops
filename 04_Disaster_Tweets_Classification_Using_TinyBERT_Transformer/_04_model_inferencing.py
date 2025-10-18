from transformers import pipeline
from pprint import pprint
import torch

model = 'TinyBERT-disaster-tweets-analysis'

#due to lib versioning issues
#device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

device = torch.device('cpu')

classifier = pipeline('text-classification', model=model, device=device)

data = [
    
    "Just saw a massive earthquake hit the city, stay safe everyone!",
    "What a beautiful day for a walk in the park.",
    "Breaking news: Wildfires are spreading rapidly, evacuations in progress.",
    "Enjoying a cup of coffee and reading a book.",
    "Severe flooding reported in several areas, avoid unnecessary travel.",
]


results=classifier(data)

pprint(results)
