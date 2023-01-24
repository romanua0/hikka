# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <  
# ---------------------------------------------------------------------------------
# Name: BFG Bunker Mod
# Description: 
# Author: romanua0
# Commands:
# .bfgb1on | .bfgb1off
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class BFGBunkerMod(loader.Module):
    """Автофарм теплиц для BFG Bunker Bot"""

    strings = {"name": "BFGBunker"}

    async def client_ready(self, client, db):
        self.db = db

    async def bfgb1oncmd(self, message):
        """Запускает фарм картошки"""
        await utils.answer(message, "<b>Запущене выращивание картошки</b>")
        status = self.db.set("BFGBunker", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("BFGBunker", "status1"):
                    return
                await message.respond("вырастить картошку")
                await sleep(600)
            status = self.db.get("BFGBunker", "status1")
            await message.respond("вырастить картошку")

    async def bfgb1offcmd(self, message):
        """Останавливает фарм картошки"""
        self.db.set("BFGBunker", "status1", False)
        await utils.answer(message, "<b>Остановлено выращивание картошки</b>")
