from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load pre-trained model and tokenizer from Hugging Face
MODEL_NAME = "t5-small"
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def summarize_text(transcription):
    # Tokenize input transcription text
    input_text = tokenizer.encode(transcription, return_tensors='pt', truncation=True, max_length=512)
    
    # Generate summary
    summary_ids = model.generate(input_ids=input_text, max_length=250, num_beams=2, early_stopping=True)
    
    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("Summary:", summary)
    
    return summary
