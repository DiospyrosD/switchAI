#!/usr/bin/env python3

import openai
from engines.engines import BaseCall
from engines.engines import GPT4Call
from utils.get_key import get_key
from utils.menu import menu

def main():
    # ANSI escape code to reset color to default and to set colors
    reset = "\033[0m"
    green = f"\033[38;5;46m"
    openai.api_key = get_key()
    my_chat = BaseCall()
    print(f"Simply ask a question to use the default settings.\nEnter \"{green}gpt-4{reset}\", \"{green}gpt-4-t{reset}\", \"{green}gpt-3{reset}\", or \"{green}gpt-3-i{reset}\" to switch between engines.\nEnter \"{green}config{reset}\" to adjust configuration settings.\nEnter a single \"{green}`{reset}\" to add multiline input (i.e., code).\nEnter \"{green}clear{reset}\" to clear your chat cache and save money!\nEnter \"{green}less{reset}\" or \"{green}vim{reset}\" to view your entire chat history.\nEnter \"{green}cache{reset}\" to view your message cache.\nEnter \"{green}quit{reset}\" to quit.")
    menu(my_chat)

if __name__ == "__main__":
    main()
