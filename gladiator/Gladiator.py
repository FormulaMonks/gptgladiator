import concurrent.futures
import json
import ast 
from gladiator import prompts
from gladiator import mocks
from typing import Any, Iterator
import openai as openai
from gladiator.GPTModel import GptModel
from gladiator.ChatBot import ChatBot


class Gladiator():
    mock_responses = False
    mock_grades = False

    def __init__(self, api_key, n=3):
        openai.api_key = api_key
        self.generate_model = GptModel('gpt-3.5-turbo', 4000)
        self.grade_model = GptModel('gpt-4', 8000)
        self.drafts = []
        self.grades = []
        self.n = n


    def drafts(self):
        return self.drafts
    

    def grades(self):
        return self.grades
    

    def process(self, tuple):
        i, prompt = tuple
        temperature = 1-i*.1
        print("temperature = ", temperature)
        chatbot = ChatBot(self.generate_model, temperature=temperature, messages=[])
        response = chatbot.get_completion(prompt)
        return response


    def concurrent_requests(self, prompts, max_active_tasks=10) -> Iterator[Any]:
        max_active_tasks = len(prompts) if len(prompts) < max_active_tasks else max_active_tasks
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_active_tasks) as executor:
            results = executor.map(self.process, enumerate(prompts))
        return list(results)
 

    def generate_drafts(self, prompt):
        print(f"running: {self.n} times with prompt: {prompt}")
        prompts = [prompt] * self.n
        drafts = self.concurrent_requests(prompts) if not self.mock_responses else mocks.mock_responses
        self.drafts = drafts
        #print("drafts = ", drafts)
        return drafts


    def grade_drafts(self, drafts):
        gradingbot = ChatBot(self.grade_model, messages=[])
        response = gradingbot.get_completion(prompts.make_grading_prompt(drafts)) if not self.mock_grades else mocks.mock_grades
        print("response to parse to json = ", response)
        grades_json = parse_json(response)
        self.grades = grades_json
        print("grades = ", grades_json)
        return grades_json


    def select_winner(self, drafts, grades_json):
        winning_index = max(range(len(grades_json)), key=lambda i: int(grades_json[str(i + 1)]['score']))
        print("winning_index = ", winning_index)
        winning_content = drafts[winning_index]
        #print("winning content = ", winning_content)
        return winning_index, winning_content
    

    def run(self, prompt: str):
        drafts = self.generate_drafts(prompt)
        grades_in_json = self.grade_drafts(drafts)
        winning_index, winning_content = self.select_winner(drafts, grades_in_json)
        return winning_content


def parse_json(json_response: str) -> dict:
    try:
        return json.loads(json_response)
    except Exception as e:
        print(f'Error parsing the json response. \n'
              f'{e}\n'
              f'Defaulting to literal eval.')
        return ast.literal_eval(json_response)



