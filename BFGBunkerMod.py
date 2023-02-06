# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <  
# ---------------------------------------------------------------------------------
# Name: BFG Bunker Mod
# Description: 
# Author: romanua0
# Commands:
# .bfgb1on | .bfgb1off | .bfgb2on | .bfgb2off | .bfgb3on | .bfgb3off
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
        """Останавливает фарм морковь"""
        self.db.set("BFGBunker", "status1", False)
        await utils.answer(message, "<b>Остановлено выращивание картошку</b>")
        
    async def bfgb2oncmd(self, message):
        """Запускает фарм морковь"""
        await utils.answer(message, "<b>Запущене выращивание морковь</b>")
        status = self.db.set("BFGBunker", "status2", True)
        while status:
            for i in range(15):
                if not self.db.get("BFGBunker", "status2"):
                    return
                await message.respond("вырастить морковь")
                await sleep(600)
            status = self.db.get("BFGBunker", "status2")
            await message.respond("вырастить морковь")

    async def bfgb2offcmd(self, message):
        """Останавливает фарм морковь"""
        self.db.set("BFGBunker", "status2", False)
        await utils.answer(message, "<b>Остановлено выращивание морковь</b>")

    async def bfgb3oncmd(self, message):
        """Запускает фарм баклажана"""
        await utils.answer(message, "<b>Запущене выращивание баклажана</b>")
        status = self.db.set("BFGBunker", "status3", True)
        while status:
            for i in range(15):
                if not self.db.get("BFGBunker", "status3"):
                    return
                await message.respond("вырастить баклажан")
                await sleep(600)
            status = self.db.get("BFGBunker", "status3")
            await message.respond("вырастить баклажан")

    async def bfgb3offcmd(self, message):
        """Останавливает фарм баклажана"""
        self.db.set("BFGBunker", "status3", False)
        await utils.answer(message, "<b>Остановлено выращивание баклажана</b>")
        
          async def bfgb4oncmd(self, message):
        """Запускает фарм перця"""
        await utils.answer(message, "<b>Запущене выращивание перця</b>")
        status = self.db.set("BFGBunker", "status4", True)
        while status:
            for i in range(15):
                if not self.db.get("BFGBunker", "status4"):
                    return
                await message.respond("вырастить перец")
                await sleep(600)
            status = self.db.get("BFGBunker", "status4")
            await message.respond("вырастить перец")

    async def bfgb4offcmd(self, message):
        """Останавливает фарм перця"""
        self.db.set("BFGBunker", "status4", False)
        await utils.answer(message, "<b>Остановлено выращивание перця</b>")
