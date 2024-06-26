## Importing pipeline from transformers package
from transformers import pipeline

## Setting up a sentiment analysis classifier
classifier = pipeline(task = "sentiment-analysis", 
                     model = "distilbert-base-uncased-finetuned-sst-2-english")

## YOUR SOLUTION HERE ##

print(classifier)

## Some sample text
sample_text =  ["I've been waiting to learn about transformers my whole life.",
               "I hate this so much!"]

## YOUR SOLUTION HERE ##

classifier(sample_text)