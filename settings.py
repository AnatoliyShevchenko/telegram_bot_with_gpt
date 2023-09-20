# Aiogram
from aiogram import Bot, Dispatcher

# Langchain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Python
import logging

# Third-Party
from decouple import config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config('TOKEN'))
dp = Dispatcher()
memory = ConversationBufferMemory()
llm = OpenAI(openai_api_key=config('API_TOKEN'))
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=ConversationBufferMemory()
)

