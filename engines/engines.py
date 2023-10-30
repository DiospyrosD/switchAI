#!/usr/bin/env python3

import openai

class BaseCall:
    def __init__(self, model_id="gpt-3.5-turbo", context_value="make responses as brief as possible; this is for testing only"):
        self.model_id = model_id
        self.context_value = context_value
        self.chat_history = None
        self.messages_list = [{"role":"system", "content": self.context_value}]
        self.prompt_token_list = []
        self.completion_token_list = []
        
    def build_call_history(self, question, messages_list):
        self.messages_list = messages_list
        if self.chat_history:
            # Append the chat_history to messages_list
            self.messages_list.append({"role": "assistant", "content": self.chat_history[0]})
            self.user_role = {"role": "user", "content": question}
            self.messages_list.append(self.user_role)
        else:
            # Build a new messages_list with the user's question
            self.user_role = {"role": "user", "content": question}
            self.messages_list.append(self.user_role)
        self.completion = openai.ChatCompletion.create(
            model=self.model_id,
            messages=self.messages_list
        )
        #print(self.messages_list) #uncomment if you wish to see messages_list cache upon each return
        return self.completion

    def retain_chat(self):
        return self.messages_list
        
    def call_api_history(self, question, messages_list):
        self.completion = self.build_call_history(question, messages_list)
        self.chat_history = [self.completion.choices[0].message.content, self.completion.usage["prompt_tokens"], self.completion.usage["completion_tokens"]]
        self.prompt_token_list.append(self.chat_history[1])
        self.completion_token_list.append(self.chat_history[2])
        self.prompt_cost = sum(self.prompt_token_list)*0.0000015
        self.completion_cost = sum(self.completion_token_list)*0.000002
        self.total_cost = self.prompt_cost+self.completion_cost
        return self.chat_history

    def configure_context(self, new_context_value):
        self.context_value = new_context_value
        self.messages_list[0] = {"role":"system", "content": self.context_value}
        
class GPT4Call(BaseCall):
    def __init__(self):
        super().__init__()
        self.model_id="gpt-4"
    
    def call_api_history(self, question, messages_list):
        self.completion = self.build_call_history(question, messages_list)
        self.chat_history = [self.completion.choices[0].message.content, self.completion.usage["prompt_tokens"], self.completion.usage["completion_tokens"]]
        self.prompt_token_list.append(self.chat_history[1])
        self.completion_token_list.append(self.chat_history[2])
        self.prompt_cost = sum(self.prompt_token_list)*0.00003
        self.completion_cost = sum(self.completion_token_list)*0.00006
        self.total_cost = self.prompt_cost+self.completion_cost
        return self.chat_history