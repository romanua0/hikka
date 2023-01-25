# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: MineEVO
# Description: Автофарм для бота MineEVO
# Author: romanua0
# Commands:
# .mineeon | .mineeoff | .minee4on | .minee4off
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class MineEVOMod(loader.Module):
    """Автофарм для бота MineEVO"""

    strings = {"name": "MineEVO"}

    async def client_ready(self, client, db):
        self.db = db

    async def mineeoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Запущено</b>")
        status = self.db.set("MineEVO", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("MineEVO", "status1"):
                    return
                await message.respond("коп")
                await sleep(2)
            status = self.db.get("MineEVO", "status1")
            await message.respond("Профиль")

    async def mineeoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("MineEVO", "status1", False)
        await utils.answer(message, "<b>Остановлено</b>")
        
            async def minee4oncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Запущено 4с</b>")
        status = self.db.set("MineEVO", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("MineEVO", "status1"):
                    return
                await message.respond("Копать")
                await sleep(4)
            status = self.db.get("MineEVO", "status1")
            await message.respond("Проф")

    async def minee4offcmd(self, message):
        """Insert info about command here... """
        self.db.set("MineEVO", "status1", False)
        await utils.answer(message, "<b>Остановлено 4с</b>")
