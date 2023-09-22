from langchain.prompts import PromptTemplate


# Prompts
prompt_begin: PromptTemplate = PromptTemplate(
    input_variables=['history', 'input'],
    template="""Представься как консультант по продаже 
автомобилей, подбери клиенту автомобиль по его потребностям и 
попытайся убедить его купить данный автомобиль, предоставляй 
конкретные марки автомобилей и их характеристики, 
веди диалог короткими вопросами. Выдавай только свои реплики 
без вопросов пользователя.

Current conversation:
{history}
Human: {input}
AI:"""
)

# Commands
commands: dict[str,str] = {
    'start' : """Команда /start начинает диалог с ботом. Если
пытаться что нибудь вводить до этой команды, 
будет вызываться команда /help""",
    'help' : """Команда /help описывает ту команду которую 
вы выполнили, или же вы начали что-то вводить перед командой /start."""
}

# Errors/Exceptions
NETWORK_ERROR: str = 'Something went wrong, try again later.'

