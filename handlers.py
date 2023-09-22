# Aiogram
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramNetworkError

# Local
from settings import memory, conversation
import constants as const


class ModuleFSM(StatesGroup):
    """Class for states storage."""

    gpt = State() # this is state for FSM


async def hello(message: types.Message, state: FSMContext):
    """This is a hello function - recieve "/start" command,
    send prompt to chatGPT and return the answer."""
    try:
        await state.set_state(ModuleFSM.gpt) # set state for awaiting user's input
        prediction = await conversation.apredict(input='Привет') # send prompt to GPT and recieving response
        await message.answer(text=prediction) # send response from GPT to user
    except TelegramNetworkError:
        await message.answer(
            text=const.NETWORK_ERROR
        )    

async def dialog(message: types.Message):
    """This is a dialog function - send and recieve text between GPT and user."""
    try:
        prediction = await conversation.apredict(input=message.text) # send text to GPT and back
        await message.answer(text=prediction) # send response from GPT to user
    except TelegramNetworkError:
        await message.answer(
            text=const.NETWORK_ERROR
        )

async def help(message: types.Message):
    """Help function - must worked if state is not GPT."""
    values = const.commands.values()
    response = '\n\n'.join(values)
    try:
        await message.answer(response)
    except TelegramNetworkError:
        await message.answer(
            text=const.NETWORK_ERROR
        )

async def default(message: types.Message):
    """This function called help if not state."""
    await help(message=message)

