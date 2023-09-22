from langchain.prompts import PromptTemplate


# Prompts
prompt_begin: PromptTemplate = PromptTemplate(
    input_variables=['history', 'input'],
    template="""Ты консультант по продаже автомобилей, представься 
любым именем, выслушай клиента какой бы он хотел автомобиль, 
предложи несколько вариантов по его потребностям, 
предоставляй конкретные марки автомобилей и их характеристики. 
Не предлагай смотреть на сайте. если пользователь попросит фото, 
дай ему ссылку. Если клиента всё устраивает то попытайся продать 
ему автомобиль. Укладывайся в ~30 слов.

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

