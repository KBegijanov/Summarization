from transformers import pipeline

summarizer = pipeline("text-summarization", model="SkolkovoInstitute/russian_toxicity_classifier")

result = summarizer ("токсичность зашкваливает")


