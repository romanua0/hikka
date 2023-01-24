# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: MineEVO
# Description: Автофарм для бота MineEVO
# Author: romanua0
# Commands:
# .mineeon | .mineeoff | .bfgon | .bfgoff
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class MineEVOMod(loader.Module):
    """Send mes"""

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
            await message.respond("🚀Оценивать")

    async def mineeoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("MineEVO", "status1", False)
        await utils.answer(message, "<b>Остановлено</b>")

    async def bfgoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Запущено</b>")
        status = self.db.set("MineEVO", "status2", True)
        while status:
            await message.respond("копать материю")
            await sleep(60 * 5)
            status = self.db.get("MineEVO", "status2")
            if not status:
                return

    async def bfgoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("MineEVO", "status2", False)
        await utils.answer(message, "<b>Остановлено</b>")
