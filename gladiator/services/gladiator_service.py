import ast
import json
import os
from typing import List

import openai as openai
import tiktoken as tiktoken

from gladiator.helpers.prompts import openai_prompt
from gladiator.models.reply import Reply
from gladiator.models.gpt_model import GptModel
from gladiator.services.gladiator_interface import GladiatorInterface

mock_response = '''
{
 "replies": [
   {
     "id": 1,
     "answer": "John McCarthy is considered the father of AI.",
     "confidence": 95.0,
   },
   {
     "id": 2,
     "answer": "Alan Turing could be seen as an early pioneer of AI.",
     "confidence": 80.0
   },
   {
     "id": 3,
     "answer": "Marvin Minsky, a prominent AI researcher, could also be considered a father figure in AI.",
     "confidence": 75.0
   },
   {
     "id": 4,
     "answer": "Some people might consider cognitive psychologist Noam Chomsky as a contributing figure in AI's development.",
     "confidence": 60.0
   }
 ]
}
'''


def parse_json(json_response: str):
    try:
        return json.loads(json_response)
    except Exception as e:
        print(f'Error parsing the json response. \n'
              f'{e}\n'
              f'Defaulting to literal eval.')
        return ast.literal_eval(json_response)


class GladiatorService(GladiatorInterface):
    debug = True
    mock_api = True

    def __init__(self):
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        self.gpt_model = GptModel('gpt-4', 2048)

    def run(self, prompt: str) -> (bool, str, List[Reply]):
        question = openai_prompt.format(question=prompt, n=4)
        messages = []
        if self.mock_api:
            json_response = mock_response
        else:
            success, error = self._call_openai(question, messages)
            if success:
                json_response = str(messages[1]['content'])
            else:
                return success, error, []

        json_response = parse_json(json_response)
        replies = [Reply(r['id'], r['answer'], r['confidence']) for r in json_response['replies']]
        return True, '', replies

    def _call_openai(self, prompt, messages) -> (bool, str):
        messages.append({'role': 'user', 'content': prompt})

        current_tokens_used = self.count_total_tokens_in_messages(messages)
        response_tokens = self.gpt_model.tokens - current_tokens_used

        if self.debug:
            print(f'Token limit: {self.gpt_model.tokens}')
            print(f'Send Token Count: {current_tokens_used}')
            print(f'Tokens remaining for response: {response_tokens}')
            print('------------ CONTEXT SENT TO AI ---------------')

        try:
            result = self._get_completion(messages)
            messages.append({'role': 'assistant', 'content': str(result).strip("'")})
            if self.debug:
                print('--------------- REPLY FROM OPEN AI API ----------')
                print(f'{result}')
            return True, None
        except Exception as e:
            print('Error: ', e)
            return False, e

    def _get_completion(self, messages):
        response = openai.ChatCompletion.create(
            model=self.gpt_model.name,
            messages=messages
        )
        return response.choices[0].message.content.strip()

    def count_total_tokens_in_messages(self, messages) -> int:
        num_tokens = 0
        for message in messages:
            num_tokens += self.num_tokens_from_string(message['content'])
        return num_tokens

    def num_tokens_from_string(self, string: str) -> int:
        encoding = tiktoken.encoding_for_model(self.gpt_model.name)
        num_tokens = len(encoding.encode(string))
        return num_tokens
