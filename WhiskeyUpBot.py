# ---------------------------------------------------------------------------------
#  /\_/\  
# ( o.o )  🔓 Not licensed.
#  > ^ <   
# ---------------------------------------------------------------------------------
# Name: WhiskeyUpBotFarm
# Description: Send mes
# Author: romanua0
# Commands:
# .whisfarmon | .whisfarmoff
# ---------------------------------------------------------------------------------




from .. import utils, loader
from asyncio import sleep

@loader.tds
class WhiskeyUpMod(loader.Module):
    """Фарм виски в Вискиметр"""

    strings = {"name": "WhiskeyUpBotFarm"}

    async def client_ready(self, client, db):
        self.db = db

    async def whisfarmoncmd(self, message):
        """Insert info about command here... """
        await utils.answer(message, "<b>Начинаю пить виски</b>")
        status = self.db.set("WhiskeyUp", "status1", True)
        while status:
            for i in range(15):
                if not self.db.get("WhiskeyUp", "status1"):
                    return
                await message.respond("/whiskey@WhiskeyUseBot")
                await sleep(3602)
            status = self.db.get("WhiskeyUp", "status1")
            await message.respond("/whiskey@WhiskeyUseBot")

    async def whisfarmoffcmd(self, message):
        """Insert info about command here... """
        self.db.set("WhiskeyUp", "status1", False)
        await utils.answer(message, "<b>Прекращаю пить виски</b>")
