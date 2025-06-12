from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, OpenAIServerModelfrom smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, OpenAIServerModel
from smolagents.agents import ToolCallingAgent
from smolagents import tool
from typing import Optional
model = LiteLLMModel(
            model_id="meta/llama3-70b-instruct",
#            model_id="qwen/qwen2.5-coder-32b-instruct",
            api_base="https://integrate.api.nvidia.com/v1",
            api_key="add key here",
            flatten_messages_as_text=True
        )
agent = CodeAgent (tools=[], model=model, add_base_tools=True)
agent.run("Find the best hotel rates for a trip to New Hampshire starting June 1st.")

#from openai import OpenAI
#client = OpenAI(
#        base_url = "https://integrate.api.nvidia.com/v1",
#        api_key = ""
#        )

#completion = client.chat.completions.create(
#        model="qwen/qwen2.5-coder-32b-instruct",
#        messages=[{"role":"user","content":"what is the 118th number in the fibonacci sequence?"}],
#        temperature=0.2,
#        top_p=0.7,
#        max_tokens=1024,
#        stream=True
#        )
#for chunk in completion:
#    if chunk.choices[0].delta.content is not None:
#        print(chunk.choices[0].delta.content, end="")
from smolagents.agents import ToolCallingAgent
from smolagents import tool
from typing import Optional
model = LiteLLMModel(
            model_id="meta/llama3-70b-instruct",
#            model_id="qwen/qwen2.5-coder-32b-instruct",
            api_base="https://integrate.api.nvidia.com/v1",
            api_key="",
            flatten_messages_as_text=True
        )
agent = CodeAgent (tools=[], model=model, add_base_tools=True)
agent.run("Find the best hotel rates for a trip to New Hampshire starting June 1st.")

#from openai import OpenAI
#client = OpenAI(
#        base_url = "https://integrate.api.nvidia.com/v1",
#        api_key = ""
#        )

#completion = client.chat.completions.create(
#        model="qwen/qwen2.5-coder-32b-instruct",
#        messages=[{"role":"user","content":"what is the 118th number in the fibonacci sequence?"}],
#        temperature=0.2,
#        top_p=0.7,
#        max_tokens=1024,
#        stream=True
#        )
#for chunk in completion:
#    if chunk.choices[0].delta.content is not None:
#        print(chunk.choices[0].delta.content, end="")

~                                                                                                                                                                                                                                            ~                                                                                                                                                                                                                                            ~                                                                                                                                                                                                                                            ~                                                                                                  
