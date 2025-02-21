import ollama
import ast

def create_question():
    """
    Generate a message (in this case a question in dictionary format) with LLM
    """
    content = ("Write only this json format: "
               "{'question': 'question', 'A': 'answer', 'B': 'answer', 'C': 'answer', 'D': 'answer', "
               "'correct': 'the correct answer (letter A,B,C or D)', 'points': 'points from 0 to 100'}"
               "create a question regarding Python or Django with different possible answers "
               "but only with one correct answer.")

    stream = ollama.chat(
        model='gemma2:2b',
        messages=[{'role': 'user', 'content': content}],
    )
    result = stream['message']['content']
    result = result.replace('```json', '').replace('```', '')
    result_dict = ast.literal_eval(result)
    return result_dict
