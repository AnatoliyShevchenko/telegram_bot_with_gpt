# Aiogram
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramNetworkError

# Local
from src.settings import Bot, conversation
import src.constants as const


class ModuleFSM(StatesGroup):
    """Class for states storage."""

    gpt = State() # this is state for FSM


async def hello(message: types.Message, state: FSMContext, bot: Bot):
    """This is a hello function - recieve "/start" command,
    send prompt to chatGPT and return the answer."""
    chat_id = message.from_user.id
    try:
        await state.set_state(ModuleFSM.gpt) # set state for awaiting user's input
        prediction = await conversation.apredict(input='Привет') # send prompt to GPT and recieving response
        await bot.send_message(
            chat_id=chat_id,
            text=prediction
        )
    except TelegramNetworkError:
        await message.answer(
            text=const.NETWORK_ERROR
        )    

async def dialog(message: types.Message, bot: Bot):
    """This is a dialog function - send and recieve text between GPT and user."""
    chat_id = message.from_user.id
    try:
        prediction = await conversation.apredict(input=message.text) # send text to GPT and back
        await bot.send_message(
            chat_id=message.from_user.id,
            text=prediction
        )
    except TelegramNetworkError:
        await message.answer(
            text=const.NETWORK_ERROR
        )

async def help(message: types.Message, bot: Bot):
    """Help function - must worked if state is not GPT."""
    values = const.commands.values()
    response = '\n\n'.join(values)
    try:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=response
        )
    except TelegramNetworkError:
        await message.answer(
            text=const.NETWORK_ERROR
        )

async def default(message: types.Message, bot: Bot):
    """This function called help if not state."""
    await help(message=message, bot=bot)

