from loader import dp,bot,zalety
from aiogram import types
from keyboards import social_check_keyboard
from utils import database



@dp.message_handler(text='🔍 Найти сливы 🔍')
async def find_leaks(message: types.Message):
    text=f'''👋 Привет, {message.from_user.full_name}\n\nЭтот бот может найти приватные фотографии девушек, анализируя их профили во всех социальных сетях и в слитых базах данных 😏\n\n🔎 Отправьте боту ссылку на страничку ВКонтакте или Instagram, или отправьте номер телефона (What\'s App/Viber/Telegram)  🔞👇'''
    photo='https://sun9-18.userapi.com/impg/3xn4BHggsVfxVb55sLbXOVDgNVqJE0t_pbchbw/f4Zkc6MgZSU.jpg?size=640x640&quality=95&sign=e6f8c1e2180063b2d5984c33428a28b8&type=album'
    await message.answer_photo(photo, text)
    await message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)

@dp.callback_query_handler(text='instagram')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте ссылку на профиль instagram</b>\n\nПримеры:\nhttps://www.instagram.com/karna.val/\ninstagram.com/samoylovaoxana/', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='vk')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте ссылку на профиль ВКонтакте</b>\n\nПримеры:\nhttps://vk.com/id494445129\nvk.com/id173811890', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='phone_number')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте номер телефона, начинающийся с +</b>\n\n+7...\n+3...', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='tiktok')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Отправте никнейм пользователя</b>\n\nПримеры:\n@karinakross\n@buzova86', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='social_back')
async def back(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥 Выбери, где будем искать', reply_markup=social_check_keyboard.keyboard)