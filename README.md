# switch-AI
A Python script built for Linux that seamlessly switches between GPT engines (gpt-4, gpt-4-1106-preview, gpt-3.5-turbo-1106, and gpt-3.5-turbo-instruct), among other features, whilst maintaining a conversation history.

# prerequisites
python3, pip, openai `pip install openai`, and boto3 `pip install boto3` (if you are using AWS Paramater Store to secure your API key).

# API-key
You will need an OpenAI API Key. I secured my key using an AWS Advanced Parameter (see the utils.get_key function). Choose your preferred method to define/secure openai.api_key.

# features
* A calculator that reports the total cost of the entire conversation, regardless of switching engines.
* Simply ask a question to use the default settings.
* Enter "gpt-4", "gpt-4-t", "gpt-3", or "gpt-3-i" to switch between engines.
* Enter "config" to adjust configuration settings.
* Enter a single "`" to add multiline input (i.e., code).
* Enter "clear" to clear your chat cache and save money!
* Enter "less" or "vim" to view your entire chat history.
* Enter "cache" to view your message cache.
* Enter "quit" to quit.

# considerations
Upon running the script, a file containing the entire chat history is created in the /tmp directory. You will be given the option to save your chat in your current working directory upon exiting.

I have implemented multithreading because the API sometimes stalls out. If a response is not received after 45 seconds, you will be issued a new prompt. A stop_flag is sent to the old thread, but sometimes the thread continues running in the background. You'll notice this upon exiting.

I'll update the readme at some point to include all the features. Though the best way to get started is to simply use it.

I also plan to add temperature and top_p configuration changes in the near future.
