from gptgladiator.Gladiator import Gladiator
import os

gladiator = Gladiator(num_drafts=3, api_key=os.environ.get('OPENAI_API_KEY'))
winner = gladiator.run("what is a hotdog?")

print("winner = ", winner)

print("drafts generated = ", gladiator.drafts)

print("grades generated = ", gladiator.grades)
