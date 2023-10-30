#!/usr/bin/env python3
import threading

def call_api_with_timeout(api_function, args, timeout, default_value):
    reset = "\033[0m"
    red = f"\033[38;5;196m"
    result = [default_value]  # Store the result in a list to make it mutable
    stop_flag = threading.Event()
    #global timeout_check
    timeout_check = True
    def call_api():
        result[0] = api_function(*args)
    # Create a thread to execute the API call
    api_thread = threading.Thread(target=call_api)
    api_thread.start()
    # Wait for the thread to finish or timeout
    api_thread.join(timeout)
    if api_thread.is_alive():
        timeout_check = False
        stop_flag.set()
        print(f"{red}The GPT API is being rather slow.\nThe stop flag has been set on this thread and will hopefully close in the background.{reset}\n")# If the thread is still running after the timeout, consider it a timeout
        #api_thread.join()  # Wait for the thread to finish; this doesn't make sense to add this...perhaps we'llr evisit later
        #print("API call timed out")
    return result[0], timeout_check