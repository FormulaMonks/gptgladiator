openai_prompt = '''Given this question: {question}

Reply to the question above. Return your response in JSON with the following structure:

{{
 "replies": [
   {{
     "id": 1,
     "answer": "First answer to the question",
     "confidence": 50.43
   }},
   {{
    "id": 2,
     "answer": "A second answer to the question",
     "confidence": 90.55
   }},
   {{
    "id": 3,
     "answer": "A third answer to the question",
     "confidence": 35.67
   }},
 ]
}}

Where the array "replies" contains {n} answers to the original question and each object sample payload has these 
properties: 
  - "id": is a unique integer you'll assign to each object in the array. 
  - "answer": is the answer in text form to the original question. Try to use no more than 200 words for this field. 
  - "confidence": is a float value between 0 and 100, with 0 being completely uncertain or confident about your answer 
  and 100 being absolutely positive.'''
