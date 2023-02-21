# scope: hikka_only
# scop: hikka_min 1.3.0

import asyncio
import logging
import time

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.events import NewMessage
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import ReadMentionsRequest
from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class BFGBMineMod(loader.Module):
    """Tasks automineng for @bfgbunker_bot"""

    strings = {"name": "BFGBMine"}

    strings_ru = {"_cls_doc": "автошахта в @bfgbunker_bot"}

    _request_timeout = 3
    _last_iter = 0
    _cache = {}

    _bot = "@bfgbunker_bot"

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "mine1",
                True,
                "Автоматическое копание песка",
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self):
        try:
            await self._client.send_message(
                self._bot,
                "💫 <i>~модуль автоматизации шахти в bfgbunker от romanua0 запущен~~</i>",
            )
        except YouBlockedUserError:
            await self._client(UnblockRequest(self._bot))
            await self._client.send_message(
                self._bot,
                "💫 <i>~модуль автоматизации шахти в bfgbunker от romanua0 запущен~~</i>",
            )

    async def _fuel(self) -> bool:
        try:
            message = await self._get_msg("копать")
            if not message:
                return False

            await message.click(text='⛏ Копать')
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGBMine click")
            self.set("mine1", None)
            return False

    async def _get_msg(self, key: str) -> Message:
        async with self._client.conversation(self._bot) as conv:
            await conv.send_message(key)
            r = await conv.get_response()
            if "у вас нет кирки!" in r.raw_text:
                key = {
                    "выкопать": "mine1",
                }[key]
                self.config[f"auto{key}"] = False
                return False

            return r

    @loader.loop(interval=15, autostart=True)
    async def loop(self):
        any_ = False
        if not self.get("fee_time") or self.get("fee_time") < time.time():
            if self.config["mine1"]:
                await self._fuel()
                any_ = True
                await asyncio.sleep(5)

            if any_:
                self.set("fee_time", int(time.time() + 6 * 60))
                
        if any_:
            await self._client(ReadMentionsRequest(self._bot))
