An intuitively interfaced command line program that allows you to prompt the gpt4 API.

##why would you need this interface?
1. The API is useful if you want specific LLM paramaters such as temperature, frequency_penalty, etc.
2. it's also useful if you want to specify the specific OpenAI model you want to use. e.g. you can swap gpt-4 for gpt-3.5_turbo if you want to use that model.
4. extensibility is also great with this project since instead of the command line, you can output to your own project, e.g. a customer service chat-bot. '
5. you can provide pre-prompts to the model the user doesn't see, such as "you are a French teacher. assist the user understand their specified french text"

##How to use
1. you may need to `pip install` or `pip3 install` the appropriate libraries if any are missing. the error message should be quite clear.
2. in the same folder as the program, in your command prompt, enter: `python3 gpt4.py` or `python gpt4.py` based on your python version
3. then type in your prompt. you can write on multiple lines, write paragraphs, etc by pressing enter.
4. at the end of your prompt, input `ctrl+d` or `cmd+d`
5. wait for the API response (should be outputted promptly, based on model speed/response length)

##How it works behind the scenes
at the top, you can specify the model, temperature, max tokens, frequency penality, presence penalty and top_p that will be used by the API. 
You don't need to refer to the OpenAI documentation and can just follow the comments I've written at the top.
After the user message has been specified, the API model will then be contacted at the appropriate endpoint, and the response will be returned
