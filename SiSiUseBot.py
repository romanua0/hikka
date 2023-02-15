# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: SiSiUpBotFarm
# Description: Send mes
# Author: romanua0
# Commands:
# .sisifarmon | .sisifarmoff
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class SiSiUpMod(loader.Module):
    """Рост члена в Членометре"""

    strings = {"name": "SiSiUpBotFarm"}

    async def client_ready(self, client, db):
        self.db = db

    async def sisifarmoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Начинаю растить сиси</b>")
        status = self.db.set("SiSiUp", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("SiSiUp", "status1"):
                    return
                await message.respond("/sisi@sisiupbot")
                await sleep(3602)
            status = self.db.get("SiSiUp", "status1")
            await message.respond("/sisi@sisiupbot")

    async def sisifarmoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("SiSiUp", "status1", False)
        await utils.answer(message, "<b>Прекращаю растить сиси</b>")
