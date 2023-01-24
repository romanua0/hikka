# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: DickUpBotFarm
# Description: Send mes
# Author: romanua0
# Commands:
# .teafarmon | .teafarmoff
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class DickUpMod(loader.Module):
    """Рост члена в Членометре"""

    strings = {"name": "DickUpBotFarm"}

    async def client_ready(self, client, db):
        self.db = db

    async def dickfarmoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Начинаю растить член</b>")
        status = self.db.set("DickUp", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("DickUp", "status1"):
                    return
                await message.respond("/dick@dickupbot")
                await sleep(3602)
            status = self.db.get("DickUp", "status1")
            await message.respond("🍌")

    async def dickfarmoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("DickUp", "status1", False)
        await utils.answer(message, "<b>Прекращаю растить член</b>")
