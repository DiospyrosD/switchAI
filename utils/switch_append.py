#!/usr/bin/env python3

#this function is needed to check the question_list history and if certain conditions are met, append the last assistant response to messages_list since .retain_chat() will not contain this last response
def switch_append(question_list, switch_answer, messages_list, my_chat, timeout_check):
    if len(question_list) > 1 and question_list[-2] not in ["gpt-3", "gpt-4", "gpt3", "gpt4", "less", "vim", "cache", "config"] and switch_answer != None and len(messages_list) != 1 and timeout_check == True:
        messages_list=my_chat.retain_chat()
        #print(question_list[-1],"++++++++++++++++++++++++************")
        #print(question_list[-2],"+++++++++++++++++++++++=============**************")
        #print(question_list[-3],"+++++++++++++++++++++++=============&&&&&&&&&&&&&&&&*************")
        if len(messages_list) > 1 and question_list[-1] not in ["cache", "vim", "less"]: # and messages_list[-1] != {f"'role': 'assistant', 'content': '{switch_answer}'"}: # and question_list[-1] not in ["cache", "config", "vim", "less"]:
            messages_list.append({"role": "assistant", "content": switch_answer})
            #print(question_list[-1],"++++++++++++++++++++++++")
            #print(question_list[-2],"+++++++++++++++++++++++=============")
            #print(question_list[-3],"+++++++++++++++++++++++=============&&&&&&&&&&&&&&&&")

    #return messages_list