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
class BFGBMod(loader.Module):
    """Tasks automation for @bfgbunker_bot"""

    strings = {"name": "BFGB"}

    strings_ru = {"_cls_doc": "Фарм в @bfgbunker_bot"}

    _request_timeout = 3
    _last_iter = 0
    _cache = {}

    _bot = "@bfgbunker_bot"

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "fuel",
                True,
                "Автоматически покупать бензин",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room1",
                True,
                "Автоматически повишает уровень комнаты 1",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room2",
                True,
                "Автоматически повишает уровень комнаты 2",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room3",
                True,
                "Автоматически повишает уровень комнаты 3",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room4",
                True,
                "Автоматически повишает уровень комнаты 4",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room5",
                True,
                "Автоматически повишает уровень комнаты 5",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room6",
                True,
                "Автоматически повишает уровень комнаты 6",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room7",
                True,
                "Автоматически повишает уровень комнаты 7",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room8",
                True,
                "Автоматически повишает уровень комнаты 8",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room9",
                True,
                "Автоматически повишает уровень комнаты 9",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room10",
                True,
                "Автоматически повишает уровень комнаты 10",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room11",
                True,
                "Автоматически повишает уровень комнаты 11",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room12",
                True,
                "Автоматически повишает уровень комнаты 12",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "room13",
                True,
                "Автоматически повишает уровень комнаты 13",
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self):
        try:
            await self._client.send_message(
                self._bot,
                "💫 <i>~модуль автоматизации bfgbunker от romanua0 запущен~~</i>",
            )
        except YouBlockedUserError:
            await self._client(UnblockRequest(self._bot))
            await self._client.send_message(
                self._bot,
                "💫 <i>~модуль автоматизации bfgbunker от romanua0 запущен~~</i>",
            )

    async def _fuel(self) -> bool:
        try:
            message = await self._get_msg("бензин")
            if not message:
                return False

            await message.click(data=b"buy_fuel_409717212")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("fuel", None)
            return False

    async def _room1(self) -> bool:
        try:
            message = await self._get_msg("к 1")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_1_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room1", None)
            return False

    async def _room2(self) -> bool:
        try:
            message = await self._get_msg("к 2")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_2_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room2", None)
            return False

    async def _room3(self) -> bool:
        try:
            message = await self._get_msg("к 3")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_3_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room3", None)
            return False

    async def _room4(self) -> bool:
        try:
            message = await self._get_msg("к 4")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_4_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room4", None)
            return False

    async def _room5(self) -> bool:
        try:
            message = await self._get_msg("к 5")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_5_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room5", None)
            return False

    async def _room6(self) -> bool:
        try:
            message = await self._get_msg("к 6")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_6_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room6", None)
            return False

    async def _room7(self) -> bool:
        try:
            message = await self._get_msg("к 7")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_7_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room7", None)
            return False

    async def _room8(self) -> bool:
        try:
            message = await self._get_msg("к 8")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_8_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room8", None)
            return False

    async def _room9(self) -> bool:
        try:
            message = await self._get_msg("к 9")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_9_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room9", None)
            return False

    async def _room10(self) -> bool:
        try:
            message = await self._get_msg("к 10")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_10_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room10", None)
            return False

    async def _room11(self) -> bool:
        try:
            message = await self._get_msg("к 11")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_11_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room11", None)
            return False

    async def _room12(self) -> bool:
        try:
            message = await self._get_msg("к 12")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_12_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room12", None)
            return False

    async def _room13(self) -> bool:
        try:
            message = await self._get_msg("к 13")
            if not message:
                return False

            await message.click(data=b"upgrade_room_409717212_13_1")
            await asyncio.sleep(1)
            return True
        except Exception:
            logger.exception("Can't process BFGB click")
            self.set("room13", None)
            return False

    async def _get_msg(self, key: str) -> Message:
        async with self._client.conversation(self._bot) as conv:
            await conv.send_message(key)
            r = await conv.get_response()
            if "чтобы построить введите команду" in r.raw_text:
                key = {
                    "бензина": "fuel",
                    "Теплица": "room1",
                    "Генераторная": "room2",
                    "Столовая": "room3",
                    "Станция": "room4",
                    "Сейф": "room5",
                    "Игровая": "room6",
                    "Медпункт": "room7",
                    "Радиостанция": "room8",
                    "Оружейная": "room9",
                    "Спортзал": "room10",
                    "Гостиная": "room11",
                    "Шахта": "room12",
                    "Лаборатория": "room13",
                }[key]
                self.config[f"auto{key}"] = False
                return False

            return r

    @loader.loop(interval=15, autostart=True)
    async def loop(self):
        any_ = False
        if not self.get("fee_time") or self.get("fee_time") < time.time():
            if self.config["fuel"]:
                await self._fuel()
                any_ = True
                await asyncio.sleep(5)
                
            if self.config["room1"]:
                await self._room1()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room2"]:
                await self._room2()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room3"]:
                await self._room3()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room4"]:
                await self._room4()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room5"]:
                await self._room5()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room6"]:
                await self._room6()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room7"]:
                await self._room7()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room8"]:
                await self._room8()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room9"]:
                await self._room9()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room10"]:
                await self._room10()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room11"]:
                await self._room11()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room12"]:
                await self._room12()
                any_ = True
                await asyncio.sleep(5)

            if self.config["room13"]:
                await self._room13()
                any_ = True
                await asyncio.sleep(5)

            if any_:
                self.set("fee_time", int(time.time() + 60 * 60))
                
        if any_:
            await self._client(ReadMentionsRequest(self._bot))
