import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from transformers import pipeline
classifier = pipeline('sentiment-analysis', model='distilbert/distilbert-base-uncased-finetuned-sst-2-english', revision='af0f99b')

res = classifier("My dog died Today")

print(res)