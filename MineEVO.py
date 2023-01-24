# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: MineEVO
# Description: Send mes
# Author: romanua0
# Commands:
# .mineeon | .mineeoff | .bfgon | .bfgoff
# ---------------------------------------------------------------------------------


# meta developer: @romanua0

from .. import utils, loader
from asyncio import sleep


class MineEVO(loader.Module):
    """Send mes"""

    strigs = {"name": "MineEVO"}

    async def client_ready(self, client, db):
        self.db = db

    async def mineeoncmd(self, message):
        """ """
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
        """ """
        self.db.set("MineEVO", "status1", False)
        await utils.answer(message, "<b>Остановлено</b>")

    async def bfgoncmd(self, message):
        """ """
        await utils.answer(message, "<b>Запущено</b>")
        status = self.db.set("MineEVO", "status2", True)
        while status:
            await message.respond("копать материю")
            await sleep(60 * 5)
            status = self.db.get("MineEVO", "status2")
            if not status:
                return

    async def bfgoffcmd(self, message):
        """ """
        self.db.set("MineEVO", "status2", False)
        await utils.answer(message, "<b>Остановлено</b>")