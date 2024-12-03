from textblob import TextBlob

generated_text = "小说我想写本"
blob = TextBlob(generated_text)
corrected_text = blob.correct()
print(corrected_text)