# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: Xyu_Epta_BotFarm
# Description: Send mes
# Author: romanua0
# Commands:
# .xyufarmon | .xyufarmoff
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class XyuMod(loader.Module):
    """Рост члена в Дрочмейстер"""

    strings = {"name": "XyuBotFarm"}

    async def client_ready(self, client, db):
        self.db = db

    async def xyufarmoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Начинаю растить хуй</b>")
        status = self.db.set("Xyu", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("Xyu", "status1"):
                    return
                await message.respond("/dick@xyu_epta_bot")
                await sleep(21602)
            status = self.db.get("Xyu", "status1")
            await message.respond("🍆")

    async def xyufarmoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("Xyu", "status1", False)
        await utils.answer(message, "<b>Прекращаю растить хуй</b>")
