# by @romanua0, 2023

import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message


@loader.tds
class TeaFarmMod(loader.Module):
    """Помошник для Чат заразки"""

    strings = {
        "name": "TeaFarm",
        "fteaon": "<i>✅Отложенка создана, автопитие запущено, всё начнётся через 10 секунд...</i>",
        "fteaon_already": "<i>Уже запущено</i>",
        "fteaoff": "<i>❌Автопитие остановлено.\n🍵Випил:</i> <b>%zar%</b>",
        "ftea": "<i>🍵Випил:</i> <b>%teas%</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id
        self.teafarm = 1785204620

    async def fteaoncmd(self, message):
        """Запустить авточай"""
        status = self.db.get(self.name, "status", False)
        if status:
            return await message.edit(self.strings["fteaon_already"])
        self.db.set(self.name, "status", True)
        await self.client.send_message(
            self.teafarm, "/tea@TeaUseBot", schedule=timedelta(seconds=10)
        )
        await message.edit(self.strings["fteaon"])

    async def fteaoffcmd(self, message):
        """Остановить авточай"""
        self.db.set(self.name, "status", False)
        teas = self.db.get(self.name, "teas", 0)
        if teas:
            self.db.set(self.name, "teas", 0)
        await message.edit(self.strings["fteaoff"].replace("%teas%", str(teas)))

    async def fteacmd(self, message):
        """Вывод кол-ва випитого чая этим модулем"""
        teas = self.db.get(self.name, "teas", 0)
        await message.edit(self.strings["ftea"].replace("%teas%", str(teas)))

    async def watcher(self, event):
        if not isinstance(event, Message):
            return
        chat = utils.get_chat_id(event)
        if chat != self.teafarm:
            return
        status = self.db.get(self.name, "status", False)
        if not status:
            return
        if event.raw_text == "/tea@TeaUseBot":
            return await self.client.send_message(
                self.teafarm, "/tea@TeaUseBot", schedule=timedelta(minutes=random.randint(60, 60))
            )
        if event.sender_id != self.teafarm:
            return
        if "через" in event.raw_text:
            args = [int(x) for x in event.raw_text.split() if x.isnumeric()]
            randelta = random.randint(20, 30)
            if len(args) == 4:
                delta = timedelta(
                    hours=args[1], minutes=args[2], seconds=args[3] + randelta
                )
            elif len(args) == 3:
                delta = timedelta(minutes=args[1], seconds=args[2] + randelta)
            elif len(args) == 2:
                delta = timedelta(seconds=args[1] + randelta)
            else:
                return
            sch = (
                await self.client(
                    functions.messages.GetScheduledHistoryRequest(self.teafarm, 1488)
                )
            ).messages
            await self.client(
                functions.messages.DeleteScheduledMessagesRequest(
                    self.teafarm, id=[x.id for x in sch]
                )
            )
            return await self.client.send_message(self.teafarm, "/tea@TeaUseBot", schedule=delta)
        if "выпил(а)" in event.raw_text or "выпил(а)" in event.raw_text:
            args = event.raw_text.split()
            for x in args:
                if x[0] == "-":
                    return self.db.set(
                        self.name,
                        "teas",
                        self.db.get(self.name, "teas", 0) + int(x[1:]),
                    )