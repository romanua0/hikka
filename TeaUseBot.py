# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: TeaUseBotFarm
# Description: Send mes
# Author: romanua0
# Commands:
# .teafarmon | .teafarmoff
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class TeaFarmMod(loader.Module):
    """Фарм чая в Чайометр"""

    strings = {"name": "TeaUseBotFarm"}

    async def client_ready(self, client, db):
        self.db = db

    async def teafarmoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Начинаю пить чай</b>")
        status = self.db.set("TeaFarm", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("TeaFarm", "status1"):
                    return
                await message.respond("/tea@TeaUseBot")
                await sleep(3602)
            status = self.db.get("TeaFarm", "status1")
            await message.respond("🍵")

    async def teafarmoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("TeaFarm", "status1", False)
        await utils.answer(message, "<b>Прекращаю пить чай</b>")
