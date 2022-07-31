from .. import loader, utils
from asyncio import sleep

class TimertMod(loader.Module):
	strings = {"name": "TimeBot"}
	async def timebcmd(self, message):
		 """Пример ввода: .timeb (частота появления текста в минуту) (текст)"""
		 await message.edit("<b>Модуль TimeBot запущен!\n\nЧтобы его остановить, используй .restart (в будущем будет функция остановки по команде).</b>")
		 args = utils.get_args_raw(message)
		 text = args.split(" ")
		 time = int(text[0]) * 60
		 time1 = time * 2
		 word = text[1:]
		 word = " ".join(word)
		 while True:
		 	await message.respond(word)
		 	await sleep(0.1)
		 	await sleep(time)		