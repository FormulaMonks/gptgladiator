def make_grading_prompt(input):
    return f'''
    You previously generated these respones: {input}

    Evaluate the above responses using the following logic:

    - Pick the best answer considering how well does it fit the original prompt
    - Assign a score to the one you selected as the best answer
    - Then grade the other answers with a score relative the one with the best score

    Take into account:
    It is accurate and factual.
    It is comprehensive and informative.
    It is clear and easy to understand.
    It is relevant to the request.
    It is creative and engaging.
    The quality of the language used.
    The accuracy of the information.
    The relevance of the information to the request.
    The clarity and conciseness of the writing.
    The creativity and engagement of the writing.


    Return your response with Valid, properly escaped JSON only, with this format and 1 item per each item reviewed. It means if there are 3 items to be graded the repsonse needs 3 items with grades:

    {{
      "1": {{
            "score": ,//The score field is the score for each answer between 1 and 100. 1 means your confidence on the score you provided is very low, the reply is unknown or uncertain. No two scores can be the same. Two items cannot both be scored 100.
        and, 100 means your confidence is very high or the reply is well-known.
            "explanation": //A short explanation about your reasoning. Keep it under 100 words when possible.
      }},
      "2": {{
          "score": ,//for item 2
          "explanation": //of your score for item 2
      }},
      // and so on for items 3 and beyond...
    }}
    '''
