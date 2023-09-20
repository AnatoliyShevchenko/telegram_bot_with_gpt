# Aiogram
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

# Local
from settings import memory, conversation
import constants as const


class ModuleFSM(StatesGroup):
    """Class for states storage."""

    gpt = State() # this is state for FSM


async def hello(message: types.Message, state: FSMContext):
    """This is a hello function - recieve "/start" command,
    send prompt to chatGPT and return the answer."""
    await state.set_state(ModuleFSM.gpt) # set state for awaiting user's input
    prediction = await conversation.apredict(input=const.prompt_begin) # send prompt to GPT and recieving response
    await message.answer(text=prediction) # send response from GPT to user

async def dialog(message: types.Message):
    """This is a dialog function - send and recieve text between GPT and user."""
    old_messages = memory.load_memory_variables({}) # loading dialog
    print(old_messages) # just for test, it works
    prediction = await conversation.apredict(
        input=f'{const.prompt_dialog} {message.text}'
    ) # send text to GPT and back
    memory.save_context(
        {'input' : message.text}, {'output' : prediction}
    ) # save dialog
    await message.answer(text=prediction) # send response from GPT to user

async def help(message: types.Message):
    """Help function - must worked if state is not GPT."""
    await message.answer('This is a help function.')

async def default(message: types.Message):
    """This function called help if not state."""
    await help(message=message)

