#!/usr/bin/env python3
import datetime
import os

def create_file_with_timestamp():
    reset = "\033[0m"
    green = f"\033[38;5;46m"
    # Generate a filename based on the current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"GPT_{timestamp}.md"
    # Construct the file path in the temporary directory
    file_path = os.path.join(os.path.sep, "tmp", filename)
    # Create an empty file
    with open(file_path, "w") as file:
        pass  # The file is created and remains empty
    print(f"File {green}{file_path}{reset} created with timestamp.")
    return file_path