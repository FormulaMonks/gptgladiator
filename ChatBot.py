import time
import openai
import tiktoken
from gpt_model import GptModel

class ChatBot:

    def __init__(self, model: GptModel, messages=[], debug=False):
        self.model = model
        self.messages = messages
        self.debug = debug

    def run(self, prompt):
        self.messages.append({"role": "user", "content": prompt})

        current_tokens_used = count_total_tokens_in_messages(self.messages, self.model)
        response_tokens = self.model.tokens - current_tokens_used

        if self.debug:
            print(f"Token limit: {self.model.tokens}")
            print(f"Send Token Count: {current_tokens_used}")
            print(f"Tokens remaining for response: {response_tokens}")
            print("------------ CONTEXT SENT TO AI ---------------")

        result = ""
        try:
            result = get_completion(self.model, self.messages)
        except Exception as e:
            print("Error: ", e)

        self.messages.append({"role": "assistant", "content": result})

def get_completion(model, messages):
    response = openai.ChatCompletion.create(
        model=model.name,
        messages=messages
    )
    return response.choices[0].message.content.strip()

def count_total_tokens_in_messages(messages, model) -> int:
    return sum(num_tokens_from_string(message['content'], model.name) for message in messages)

def num_tokens_from_string(string: str, model_name: str) -> int:
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


