#!/usr/bin/env python3
import os
import sys
import subprocess
import datetime
import time
import select

from engines.engines import BaseCall
from engines.engines import GPT4Call
from engines.engines import GPT4TCall
from utils.switch_append import switch_append
from utils.call_api import call_api_with_timeout

def core_logic(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check):
    reset = "\033[0m"
    red = f"\033[38;5;196m"
    green = f"\033[38;5;46m"
    question_list.append(question)
    if question.lower() == "gpt-4" or question.lower() == "gpt4":
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        my_chat=GPT4Call()
        engine="gpt-4"
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    elif question.lower() == "gpt-4-t" or question.lower() == "gpt4t":
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        my_chat=GPT4TCall()
        engine="gpt-4-t"
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    elif question.lower() == "gpt-3" or question.lower() == "gpt3":
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        my_chat=BaseCall()
        engine="gpt-3"
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    elif question.lower() == "gpt-3-i" or question.lower() == "gpt3i":
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        my_chat=BaseCall()
        engine="gpt-3-i"
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    elif question.lower() == "quit" or question.lower() == "exit":
        print(f"Would you like to save your chat in your current working directory (yes/no)?\nIf no, you may find your chat located here {file_path}")
        ex_input = input(">")
        if ex_input.lower() == "yes":
            # Get the file's base name (without the path)
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, 'rb') as source_file, open(destination_path, 'wb') as dest_file:
                dest_file.write(source_file.read())
            print(f"File {green}{file_name}{reset} has been copied to the current directory.")
            sys.exit()
        else:
            print(f"Exiting...no worries, you can find your chat here {file_path} if you wish!")
            sys.exit()
    elif question.lower() == "clear":
        messages_list_0 = messages_list[0]
        messages_list=my_chat.retain_chat()
        if messages_list[0] != messages_list_0 and messages_list[0] != {'role': 'system', 'content': 'make responses as brief as possible; this is for testing only'}:
            messages_list_0 = messages_list[0]
        if engine == "gpt-3":
            my_chat=BaseCall()
            engine_set_clear(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, messages_list_0, file_path, timeout_check)
        elif engine == "gpt-4":
            my_chat=GPT4Call()
            engine_set_clear(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, messages_list_0, file_path, timeout_check)
        elif engine == "gpt-4-t":
            my_chat=GPT4TCall()
            engine_set_clear(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, messages_list_0, file_path, timeout_check)
        elif engine == "gpt-3-i":
            my_chat=GPT4TCall()
            engine_set_clear(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, messages_list_0, file_path, timeout_check)
    elif question.lower() == "config":
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        config_function(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
        #return engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer
    elif question.lower() == "vim":
        try:
            # Use the subprocess module to run the 'vim' command with the specified file. You can change this command to less if you prefer.
            subprocess.run(['vim', file_path], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to open '{file_path}' with vim.")
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    elif question.lower() == "less":
        try:
            # Use the subprocess module to run the 'less' command with the specified file. You can change this command to less if you prefer.
            subprocess.run(['less', '+G', file_path], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to open '{file_path}' with less.")
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    elif question.lower() == "cache":
        switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check)
        try:
            print(f"This is your cached messages_list that is sent each time a question is asked.\nType \"{green}clear{reset}\" to clear this cache and save money.\n")
            for dict_m in messages_list:
                #formatted_dict = "\n".join([f"{key}: {value}" for key, value in dict_m.items()])
                print(str(dict_m))
        except:
            print(f"Whoops!")
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    timeout_seconds = 45   #adjust if you need a longer timeout for GPT to respond
    default_result = "I'm being too slow, try again!"  # Replace with your desired default value; if you use "None" you will get an unsubscriptable error but everything still works
    answer = call_api_with_timeout(my_chat.call_api_history, (question, messages_list), timeout_seconds, default_result)
    answer = answer[0]
    if answer is not "I'm being too slow, try again!":
        total_cost=my_chat.total_cost+float(carried_total_cost) #this is where we add the carried values as we switch engines
        prompt_cost=my_chat.prompt_cost+float(carried_prompt_cost)
        completion_cost=my_chat.completion_cost+float(carried_completion_cost)
        #print("You have consumed",my_chat.prompt_token_list, "prompt tokens, which sums up to be: ",sum(my_chat.prompt_token_list)) #uncomment if you wish to see the total prompt tokens used for each engine
        #print("You have consumed",my_chat.completion_token_list, "completion tokens, which sums up to be: ",sum(my_chat.completion_token_list)) #uncomment if you wish to see the total prompt tokens used for each engine
        print(f"Your chat has a total cost of: {red}${total_cost:.20f}{reset}\n\tTotal Prompt Cost: {red}${prompt_cost:.20f}{reset}\n\tTotal Completion Cost: {red}${completion_cost:.20f}{reset}")
        print(f"\n{green}{engine.upper()}{reset} says:\n")
        print(f"{green}{answer[0]}{reset}\n")
        with open(file_path, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file.write(f"***********************************************************\n\n{engine.upper()} says at {timestamp}:\n\n\t{answer[0]}\n\n")
            file.write(f"This has a Total Cost of: ${total_cost:.20f}\n\tTotal Prompt Cost: ${prompt_cost:.20f}\n\tTotal Completion Cost: ${completion_cost:.20f}\n\n***********************************************************\n\n")
        switch_answer=answer[0]
    else:
        print("Please try again")
        (question_list, switch_answer, messages_list, my_chat, timeout_check)
        engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    return engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check
    
def take_input(engine, start_time1, file_path):
    reset = "\033[0m"
    red = f"\033[38;5;196m"
    blue = f"\033[38;5;33m"
    timeout = 20  # Set the timeout in seconds
    input_text=[]
    line1 = input(engine+">")
    start_time1.append(time.time())
    multiline = True
    if line1 != "`":
        input_text.append(line1)
        print(f"{blue}processing input, please wait...{reset}")
    if line1 == "`":
        print("Please enter a multiline input:\nIf no input is added within 20 seconds, a new single line prompt will display.\nEnter an additional carriage return to send your multiline input to ChatGPT")
        start_time2 = time.time()
        while multiline:
            remaining_time = timeout - (time.time() - start_time2)
            if remaining_time <= 0:
                print("===============timeout, please reenter multiline mode if you have input to paste=================")
                multiline = False  # Exit the loop if the timeout has been reached
                break #not sure why I have to explicitly break out of this loop; setting multiline to False doesn't break it
            rlist, _, _ = select.select([sys.stdin], [], [], remaining_time)
            if rlist:
                line = sys.stdin.readline().rstrip()
                if not line:
                    multiline = False
                    break# Exit the loop if an empty line is entered
                input_text.append(line)
        print(f"{blue}processing multiline input, please wait...{reset}")
    input_text = '\n'.join(input_text)
    if input_text == '':
        input_text = take_input(engine, start_time1, file_path)
    if multiline and len(start_time1) >= 2 and (start_time1[-1] - start_time1[-2]) < 2.2:
        print(f"{red}==============You cannot entire multiline input without being in multiline mode================{reset}")
        print(f"{red}===================================Type ` to enter multiline mode=============================={reset}")
        input_text, start_time1 = take_input(engine, start_time1, file_path)
    with open(file_path, "a") as file:
        file.write(f"\n\n>{input_text}\n\n")
    if input_text.lower() != "quit" or input_text.lower() != "exit":
        return input_text, start_time1
        
def engine_set(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check):
    reset = "\033[0m"
    green = f"\033[38;5;46m"
    print(f"AI engine set to {green}{engine.upper()}{reset}")
    carried_total_cost=total_cost
    carried_prompt_cost=prompt_cost
    carried_completion_cost=completion_cost
    start_time1 = []
    for j in range(100):
        input_text, start_time1 = take_input(engine, start_time1, file_path)
        question = input_text
        engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check=core_logic(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
        
def engine_set_clear(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, messages_list_0, file_path, timeout_check):
    reset = "\033[0m"
    green = f"\033[38;5;46m"
    messages_list = [messages_list_0]  # Keep the item at index 0 config context
    print(f"Your engine is still set to {green}{engine.upper()}{reset}.\nYou have cleared your history")
    carried_total_cost=total_cost
    carried_prompt_cost=prompt_cost
    carried_completion_cost=completion_cost
    start_time1 = []
    for j in range(100):
        input_text, start_time1 = take_input(engine, start_time1, file_path)
        question = input_text
        core_logic(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    return messages_list
    
def config_function(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check):
    reset = "\033[0m"
    green = f"\033[38;5;46m"
    new_context_value = input("Enter a new question context here:\nCONFIG#")
    if new_context_value.lower() == "quit" or new_context_value.lower() == "exit":
        sys.exit()
    else:
        new_context_value, messages_list = my_chat.configure_context(new_context_value, messages_list)
        print(f"Context value updated to: {green}{my_chat.context_value}{reset}\n")
        start_time1 = []
        #messages_list[0] = {"role":"system", "content": new_context_value}
        for j in range(100):
            input_text, start_time1 = take_input(engine, start_time1, file_path)
            question = input_text
            engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check=core_logic(question, my_chat, engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, file_path, timeout_check)
    #return engine, total_cost, prompt_cost, completion_cost, carried_total_cost, carried_prompt_cost, carried_completion_cost, messages_list, switch_answer, question_list, timeout_check
