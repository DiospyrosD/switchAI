# switch-AI
A Python script that seamlessly switches between GPT engines, among other features, whilst maintaining a conversation history.

# prerequisites
python3, pip, openai `pip install openai`, and boto3 `pip install boto3`

# API-key
You will need an OpenAI API Key. I secured my key using an AWS Advanced Parameter (see the utils.get_key function). Choose your preferred method to define/secure openai.api_key.

# features
* Simply ask a question to use the default settings.
* Enter "gpt-4" or "gpt-3" to switch between engines.
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
