# ## Importing pipeline from transformers package
# from transformers import pipeline
# import tensorflow as tf
# print(tf.__version__)

# def transformater():

#     response = {}

#     ## Setting up a sentiment analysis classifier
#     classifier = pipeline(task = "sentiment-analysis", 
#                         model = "distilbert-base-uncased-finetuned-sst-2-english")

#     ## YOUR SOLUTION HERE ##

#     print(classifier)

#     ## Some sample text
#     sample_text =  ["J'ai reussi à echouer a mon examen",
#                 "Je reprendrai l'année prochaine"]

#     ## YOUR SOLUTION HERE ##

#     response = classifier(sample_text)

#     return response