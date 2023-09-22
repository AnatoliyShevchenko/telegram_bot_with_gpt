# Aiogram
from aiogram import Bot, Dispatcher

# Langchain
from langchain.llms import OpenAI
from langchain.memory import (
    ConversationBufferMemory, 
    ConversationBufferWindowMemory,
)
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Python
import logging

# Third-Party
from decouple import config

# Local
import constants as const


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config('TOKEN'))
dp = Dispatcher()
memory = ConversationBufferWindowMemory(k=5)
llm = OpenAI(
    openai_api_key=config('API_TOKEN'), 
    max_tokens=512
)
conversation = ConversationChain(
    llm=llm, 
    memory=memory,
    prompt=const.prompt_begin,
    verbose=True
)

