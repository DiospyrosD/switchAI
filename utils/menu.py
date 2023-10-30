#!/usr/bin/env python3
from utils.create_file import create_file_with_timestamp
#from utils.take_input import take_input
from utils.core_logic import core_logic
from utils.core_logic import take_input

def menu(my_chat):
    engine ="gpt-3"
    total_cost = 0
    prompt_cost = 0
    completion_cost = 0
    carried_total_cost = 0
    carried_prompt_cost = 0
    carried_completion_cost = 0
    switch_answer = None
    messages_list = [{"role":"system", "content": "make responses as brief as possible; this is for testing only"}]
    question_list = []
    start_time1 = []
    file_path = ""
    file_path = create_file_with_timestamp()
    timeout_check = True
    for i in range(100):
        input_text, start_time1 = take_input(engine, start_time1, file_path)
        question = input_text
        engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check=core_logic(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)