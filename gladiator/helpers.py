import ast
import json
from typing import List

import tiktoken

from gladiator.models.reply import Reply

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

mock_replies = [
    {
        "choices": [
            {
                'text': "German physicist Wilhelm Röntgen is credited with the discovery of X-Rays in 1895."
            }
        ]
    },
    {
        "choices": [
            {
                'text': "The X-rays were discovered by German physicist Wilhelm Röntgen in 1895."
            }
        ]
    },
    {
        "choices": [
            {
                'text': "The German physicist Wilhelm Conrad Röntgen is credited with the discovery of X-Rays in 1895."
            }
        ]
    },
    {
        "choices": [
            {
                'text': "In 1895, German physicist Wilhelm Conrad Röntgen discovered X-rays."
            }
        ]
    }
]

grading_prompt = """
Evaluate your previous responses. Assign each one of them a confidence score between 1 and 100, 1 meaning 
completely unknown, false or uncertain and 100 meaning completely true, well-known or certain.
Return your response in JSON following the format below:
[
  {
    "idx": 1,
    "sc": 84.57
  },
  {
    "idx": 2,
    "sc": 95.63
  }
]
"""

mock_grading_response = '''
[
  {
    "idx": 1,
    "sc": 95.0
  },
  {
    "idx": 2,
    "sc": 90.0
  },
  {
    "idx": 3,
    "sc": 95.0
  },
  {
    "idx": 4,
    "sc": 59.23
  }
]
'''


def parse_json(json_response: str) -> dict:
    try:
        return json.loads(json_response)
    except Exception as e:
        print(f'Error parsing the json response. \n'
              f'{e}\n'
              f'Defaulting to literal eval.')
        return ast.literal_eval(json_response)


def save_reply(idx, text, messages: List[dict], replies: dict) -> None:
    messages.append({"role": "assistant", "content": f"{idx + 1}. {text.strip()}"})
    replies[idx + 1] = Reply(idx + 1, text)


def num_tokens_from_string(string: str, model_name: str) -> int:
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
