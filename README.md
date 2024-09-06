## Purpose
The OpenAI API is great for developers, who can use it well for their own projects, but it is unintuitive for individual use.\

1. This API Interfacer provides a platform to easily interact with OpenAI APIs, e.g. GPT-4.
2. Using this interfacer often significantly cheaper than OpenAI-Plus, since it is pay-as-you-go pricing.
3. Customisation is also possible, since the user can specify various LLM paramaters (e.g. temperature, frequency_penalty, etc.)
4. Additionally, you can specify pre-prompts, e.g. "you are a french teacher, assist the user with french".
5. Various models are available depending on budget/requirements (e.g. gpt-4, gpt-3.5_turbo, etc.
6. Modular code allows you to integrate with developer projects well (e.g. customer service chat-bot)

## Screenshot
<img width="493" alt="Screenshot 2024-09-06 at 4 13 38 pm" src="https://github.com/user-attachments/assets/cc12084a-2006-4a05-b41d-48276be1e09d">


## How to Use
```
git clone git@github.com:manav1411/gpt4API_interfacer.git
cd gpt4API_interfacer
pip3 install requests
python3 gpt4.py
# Type your specified prompt.
ctrl+d        # cmd+d on mac. when finished with prompt.
              # Await model response
```
Note: if you have issues installing requests, consider creating a python virtual env with `python3 -m venv myenv`, `source myenv/bin/activate`, `python3 gpt4.py`, then `deactivate`\

After the user message has been specified, the API model will then be contacted at the appropriate endpoint.\
You can press "enter" for new lines. multiple lines/paragraphs supported

### Modifications
If you open gpt4.py, you can specify the model, temperature, max tokens, frequency penality, presence penalty and top_p that will be used by the API.\
You don't need to refer to OpenAI documentation, and can refer to the comments I've written at the top.
