import transformers 
import nltk.tokenize 
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
MODEL_NAME = "t5-small" 
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def summarize_text(transcription):
    input_text = tokenizer.encode(transcription, return_tensors='pt', truncation=True, max_length=512)
    summary_ids = model.generate(input_ids=input_text, max_length=250, num_beams=2, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print(summary)
    return summary