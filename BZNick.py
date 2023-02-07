# meta developer: @romanua0

from .. import loader, utils
import string, pickle, re
from telethon.tl.types import Channel

conf_default = {
    "-s1": {  # СТИЛИ для действия
        "1": [False, "<b>bold/жирный</b>", "<b>", "</b>"],
        "2": [False, "<i>italic/курсив</i>", "<i>", "</i>"],
        "3": [False, "<u>underlined/подчеркнутый</u>", "<u>", "</u>"],
        "4": [False, "<s>strikethrough/зачёркнутый</s>", "<s>", "</s>"],
        "5": [
            False,
            "<tg-spoiler>spoiler/скрытый</tg-spoiler>",
            "<tg-spoiler>",
            "</tg-spoiler>",
        ],
    },
    "-s2": {  # СТИЛИ для "С репликой"
        "1": [True, "<b>bold/жирный</b>", "<b>", "</b>"],
        "2": [False, "<i>italic/курсив</i>", "<i>", "</i>"],
        "3": [False, "<u>underlined/подчеркнутый</u>", "<u>", "</u>"],
        "4": [False, "<s>strikethrough/зачёркнутый</s>", "<s>", "</s>"],
        "5": [
            False,
            "<tg-spoiler>spoiler/скрытый</tg-spoiler>",
            "<tg-spoiler>",
            "</tg-spoiler>",
        ],
    },
    "-s3": {  # СТИЛИ для реплики
        "1": [False, "<b>bold/жирный</b>", "<b>", "</b>"],
        "2": [False, "<i>italic/курсив</i>", "<i>", "</i>"],
        "3": [False, "<u>underlined/подчеркнутый</u>", "<u>", "</u>"],
        "4": [False, "<s>strikethrough/зачёркнутый</s>", "<s>", "</s>"],
        "5": [
            False,
            "<tg-spoiler>spoiler/скрытый</tg-spoiler>",
            "<tg-spoiler>",
            "</tg-spoiler>",
        ],
    },
    "-sE": {  # ЭМОДЗИ перед репликой
        "1": [True, "💬"],
        "2": [False, "💭"],
        "3": [False, "🗯"],
        "4": [False, "✉️"],
        "5": [False, "🔊"],
        "6": [False, "🗃"],
    },
    "-sS": {  # РАЗРЫВ строки в реплике
        "1": [True, "space/пробел", " "],
        "2": [False, "line break/разрыв строки", "\n"],
        "3": [False, "dot + space/точка + пробел", ". "],
        "4": [False, "comma + space/запятая + пробел", ", "],
    },
}


@loader.tds
class BZNick(loader.Module):
    """module of @romanua0."""

    strings = {
        'name': 'BZNick',
        'separator…': '<b>Here\'s an emoji separator, but no emoji. eh</b>',
        'name?': '<b>Where\'s the name of the BZNick command?</b>',
        'action?': '<b>Where\'s the action of the BZNick command?</b>',
        'aarf': '<b>BZNick commands can\'t be named "all"</b>',
        'added1': "<b>Command '<code>{}</code>' succesfully added with emoji '{}'!</b>",
        'added2': "<b>Command '<code>{}</code>' succesfully added!</b>",
        'weresall': '<b>You\'ve not entered separator or have\'nt entered anything at all.</b>',
        'cleared': '<b>BZNick commands succesfully cleared!</b>',
        'arg?': '<b>Where\'s the argument?</b>',
        'deleted': '<b>BZNick command <code>{}</code> succesfully deleted!</b>',
        'notfound': '<b>Command <code>{}</code> not found!</b>',
        'on': '<b>BZNick commands are now on!</b>',
        'off': '<b>BZNick commands are now off!</b>',
        'mode': '<b>Mode is now <code>{}</code>!</b>',
        'send': 'sending messages',
        'edit': 'editing messages',
        's-t-wrong': '<b>Something went wrong!</b>',
        'nick-changed': '<b>BZNick nickname of {} succesfully changed to <code>{}</code>!</b>',
        'count': '<b>You have <code>{}</code> commands</b>',
        'error-with-type': '<b>Error: <code>{}</code></b>',
        'itsnotfile': '<b>It\'s not a file!</b>',
        'actualised': '<b>BZNick commands succesfully actualised!</b>',
        'chat-excluded': '<b>Chat {} succesfully excluded!</b>',
        'chat-included': '<b>Chat {} succesfully included!</b>',
        'id-wrong': '<b>Wrong ID!</b>',
        'empty-exclude': '<b>Excluded chats list is empty!</b>',
        'excluded-chats': '<b>Excluded chats:</b>',
        'on-in-chat': '<b>BZNick commands are now on for members of this chat!</b>',
        'off-in-chat': '<b>BZNick commands are now off for members of this chat!</b>',
        'who-have': '<b>Who have BZNick commands access:</b>',
        'chats-s': '<b>Chats:</b>',
        'users-s': '<b>Users:</b>',
        'on-for-usr': '<b>BZNick commands are now on for <code>{}</code>!</b>',
        'off-for-usr': '<b>BZNick commands are now off for <code>{}</code>!</b>',
        'whatschanged': '''🍋 <b>BZNick</b> (1.1) — mod of BZNick by @romanua0 What\'s changed?
    • No limits now!
    • No check for emoji validity now — add custom emojies…
    • No buggy import now, everyone can use the module.
    • Additions and replicas now save there\'s case.
Enjoy!''',
        'with-replica': 'With replica:',
        'backup-args-help': '<b>Usage:</b>\n.bznickback [-b to save| -l to load (with reply)]',
        'arg-unknown': '<b>Unknown argument!</b>',
        'num-unknown': '<b>Unknown number!</b>',
        'done': '<b>Done!</b>',
        'less-then-2': '<b>Less then 2 arguments!</b>',
        'config2': '⚙️ <b>Setting up the template for command:</b>\n-s1 --- turn on/off style for action:\n{s1}\n-s2 '
                  '--- same as s1, but for "With replica" text:\n{}\n-s3 --- same as s2, but for replica:\n{}\n-sE '
                  '--- choose emoji before replica:\n{}\n-sS --- choose symbol for line break in reply:\n{'
                  '}\n\nExample:\n<code>.bznickconf -s1 2</code>',
        'config1': '⚙️ <b>Setting up the template for command:',
    }

    strings_ru = {
        'name': 'BZNick',
        'separator…': '<b>Вот разделитель, но нет эмодзи. епт</b>',
        'name?': '<b>Где имя BZNick-команды?</b>',
        'action?': '<b>Где действие BZNick-команды?</b>',
        'aarf': '<b>BZNick-команды не могут называться "all"</b>',
        'added1': "<b>Команда '<code>{}</code>' успешно добавлена с эмодзи '{}'!</b>",
        'added2': "<b>Команда '<code>{}</code>' успешно добавлена!</b>",
        'weresall': '<b>Вы не ввели разделитель или ничего не ввели вообще.</b>',
        'cleared': '<b>BZNick-команды успешно очищены!</b>',
        'arg?': '<b>Где аргумент?</b>',
        'deleted': '<b>BZNick-команда <code>{}</code> успешно удалена!</b>',
        'notfound': '<b>Команда <code>{}</code> не найдена!</b>',
        'on': '<b>BZNick-команды теперь включены!</b>',
        'off': '<b>BZNick-команды теперь выключены!</b>',
        'mode': '<b>Режим теперь <code>{}</code>!</b>',
        'send': 'отправку сообщений',
        'edit': 'редактирование сообщений',
        's-t-wrong': '<b>Что-то пошло не так!</b>',
        'nick-changed': '<b>Ник {} успешно изменен на <code>{}</code>!</b>',
        'count': '<b>У вас <code>{}</code> команд</b>',
        'error-with-type': '<b>Ошибка: <code>{}</code></b>',
        'itsnotfile': '<b>Это не файл!</b>',
        'actualised': '<b>BZNick-команды успешно обновлены!</b>',
        'chat-excluded': '<b>Чат {} успешно исключен!</b>',
        'chat-included': '<b>Чат {} успешно включен!</b>',
        'id-wrong': '<b>Неверный ID!</b>',
        'empty-exclude': '<b>Список исключённых чатов пуст!</b>',
        'excluded-chats': '<b>Исключённые чаты:</b>',
        'on-in-chat': '<b>BZNick-команды теперь включены для участников этого чата!</b>',
        'off-in-chat': '<b>BZNick-команды теперь выключены для участников этого чата!</b>',
        'who-have': '<b>Кто имеет доступ к РП-командам:</b>',
        'chats-s': '<b>Чаты:</b>',
        'users-s': '<b>Пользователи:</b>',
        'on-for-usr': '<b>BZNick-команды теперь включены для <code>{}</code>!</b>',
        'off-for-usr': '<b>BZNick-команды теперь выключены для <code>{}</code>!</b>',
        'whatschanged': '''🗃 <b>BZNick</b> — модуль BZNick от @romanua0''',
        'with-replica': 'С репликой:',
        'backup-args-help': '<b>Использование:</b>\n.bznickback [-b для сохранения | -l для загрузки (с ответом)]',
        'arg-unknown': '<b>Неизвестный аргумент!</b>',
        'num-unknown': '<b>Неизвестная цифра!</b>',
        'done': '<b>Готово!</b>',
        'less-than-2': '<b>Меньше двух аргументов передано.</b>',
        'config2': '⚙️ <b>Настройка шаблона для команды:</b>\n-s1 --- включить/выключить стиль для действия:\n{}\n-s2 '
                  '--- аналогично для s1, но действует на текст "С репликой":\n{}\n-s3 --- аналогично для s2, '
                  'но действует на саму реплику:\n{}\n-sE --- выбор эмодзи перед репликой:\n{}\n-sS --- выбор символа '
                  'для разрыва строк в реплике:\n{}\n\nПример:\n<code>.bznickconf -s1 2</code>',
        'config1': '⚙️ <b>Настройка шаблона для команды:',
        '_cls_doc': 'Слегка улучшенный мод на модуль от @romanua0.',
        '_cmd_doc_dobbznick': 'Создать BZNick-команду. Аргументы: <команда>/<действие>[/<эмодзи>]',
        '_cmd_doc_delbznick': 'Удалить BZNick-команду. Аргументы: <команда>',
        '_cmd_doc_bznicklist': 'Показать список BZNick-команд.',
        '_cmd_doc_bznickconf': 'Настроить шаблон для BZNick-команд. Аргументы: <параметр> <значение>',
        '_cmd_doc_bznickback': 'Сохранить/загрузить BZNick-команд. Аргументы: -b/-l',
        '_cmd_doc_bznicknick': 'Изменить ник для BZNick-команд. Аргументы: <ник> или без ника, чтобы его сбросить. '
                           'В ответ на сообщение нужного пользователя.',
        '_cmd_doc_bznickblock': 'Заблокировать/разблокировать BZNick-команды в чате. Аргументы: <айди чата>. '
                            'Можно и без него, чтобы сменить настройки в этом чате.',
        '_cmd_doc_bznickmod': 'Изменить режим BZNick-команд.',
        '_cmd_doc_useracceptbz': 'Допустить или нет пользователя/чат в BZNick-команды. Аргументы: <айди пользователя/чата>. '
                               'Можно без ответа и аргумента, тогда действие будет выполнена над текущим чатом. '
                               'Можно просто без аргумента , тогда действие будет выполнено над пользователем из ответа.',
        '_cmd_doc_mmminfo': 'Показать информацию о моде.',
    }

    async def client_ready(self, client, db):
        self.db = db
        if not self.db.get("BZNick", "exlist", False):
            self.db.set("BZNick", "exlist", [])
        if not self.db.get("BZNick", "status", False):
            self.db.get("BZNick", "status", 1)
        if not self.db.get("BZNick", "bznickrezjim", False):
            self.db.set("BZNick", "bznickrezjim", 1)
        if not self.db.get("BZNick", "bznicknicks", False):
            self.db.set("BZNick", "bznicknicks", {})
        if not self.db.get("BZNick", "bznickcomands", False):
            self.db.set("BZNick", "bznickcomands", {})
        if not self.db.get("BZNick", "bznickemoji", False):
            self.db.set("BZNick", "bznickemoji", {})
        if not self.db.get("BZNick", "useracceptbz", False):
            self.db.set("BZNick", "useracceptbz", {"chats": [], "users": []})
        elif type(self.db.get("BZNick", "useracceptbz")) == type([]):
            self.db.set(
                "BZNick",
                "useracceptbz",
                {"chats": [], "users": self.db.get("BZNick", "useracceptbz")},
            )
        if self.db.get("BZNick", "bznickconfigurate", False):  # ДЛЯ разных версий модуля.
            self.db.set(
                "BZNick",
                "bznickconfigurate",
                self.merge_dict(conf_default, self.db.get("BZNick", "bznickconfigurate")),
            )

    async def dobbznickcmd(self, message):
        """Use: .dobbznick (command) / (action) / (emoji) to add command. You can do it without emoji."""
        args = utils.get_args_raw(message)
        dict_bznick = self.db.get("BZNick", "bznickcomands")

        try:
            key_bznick = str(args.split("/")[0]).strip()
            value_bznick = str(args.split("/", maxsplit=2)[1]).strip()
            lenght_args = args.split("/")
            count_emoji = 0

            if len(lenght_args) >= 3:
                emoji_bznick = str(message.text.split("/", maxsplit=2)[2]).strip()
                dict_emoji_bznick = self.db.get("BZNick", "bznickemoji")
                r = emoji_bznick
                lst = []
                count_emoji = 1
                if not emoji_bznick or not emoji_bznick.strip():
                    await utils.answer(
                        message, self.strings("separator…")
                    )
                    return
            key_len = [len(x) for x in key_bznick.split()]

            if not key_bznick or not key_bznick.strip():
                await utils.answer(message, self.strings("name?"))
            elif not value_bznick or not value_bznick.strip():
                await utils.answer(
                    message, self.strings("action")
                )
            elif key_bznick == "all":
                await utils.answer(
                    message, self.strings("aarf"),
                )
            elif count_emoji == 1:
                dict_emoji_bznick[key_bznick] = emoji_bznick
                dict_bznick[key_bznick] = value_bznick
                self.db.set("BZNick", "bznickcomands", dict_bznick)
                self.db.set("BZNick", "bznickemoji", dict_emoji_bznick)
                await utils.answer(
                    message,
                    self.strings("added1").format(key_bznick, emoji_bznick),
                )
            else:
                dict_bznick[key_bznick] = value_bznick
                self.db.set("BZNick", "bznickcomands", dict_bznick)
                await utils.answer(
                    message,
                    self.strings("added2").format(key_bznick),
                )
        except:
            await utils.answer(
                message, self.strings("weresall"),
            )

    async def delbzcmd(self, message):
        """Use: .delbznick (command) to delete command.\n Use: .delbznick all to delete all commands."""
        args = utils.get_args_raw(message)
        dict_bznick = self.db.get("BZNick", "bznickcomands")
        dict_emoji_bznick = self.db.get("BZNick", "bznickemoji")
        key_bznick = str(args)
        count = 0
        if key_bznick == "all":
            dict_bznick.clear()
            dict_emoji_bznick.clear()
            self.db.set("BZNick", "bznickcomands", dict_bznick)
            self.db.set("BZNick", "bznickemoji", dict_emoji_bznick)
            await utils.answer(message, self.strings("cleared"))
            return
        elif not key_bznick or not key_bznick.strip():
            await utils.answer(message, self.strings("name?"))
        else:
            try:
                if key_bznick in dict_emoji_bznick:
                    dict_bznick.pop(key_bznick)
                    dict_emoji_bznick.pop(key_bznick)
                    self.db.set("BZNick", "bznickcomands", dict_bznick)
                    self.db.set("BZNick", "bznickemoji", dict_emoji_bznick)
                else:
                    dict_bznick.pop(key_bznick)
                    self.db.set("BZNick", "bznickcomands", dict_bznick)
                await utils.answer(
                    message, self.strings("deleted").format(key_bznick),
                )
            except KeyError:
                await utils.answer(message, self.strings("notfound"))

    async def bznickmodcmd(self, message):
        """Use: .bznickmod to turn on/off BZNick mode.\nUse: .bznickmod toggle to change mode to send or edit message."""
        status = self.db.get("BZNick", "status")
        rezjim = self.db.get("BZNick", "bznickrezjim")
        args = utils.get_args_raw(message)
        if not args:
            if status == 1:
                self.db.set("BZNick", "status", 2)
                await utils.answer(message, self.strings("off"))
            else:
                self.db.set("BZNick", "status", 1)
                await utils.answer(message, self.strings("on"))
        elif args.strip() == "toggle":
            if rezjim == 1:
                self.db.set("BZNick", "bznickrezjim", 2)
                await utils.answer(
                    message, self.strings("mode").format(self.strings("send"))
                )
            else:
                self.db.set("BZNick", "bznickrezjim", 1)
                await utils.answer(
                    message, self.strings("mode").format(self.strings("edit"))
                )
        else:
            await utils.answer(message, self.strings("s-t-wrong"))

    async def bznicklistcmd(self, message):
        """Use: .bznicklist to see list of BZNick commands."""
        com = self.db.get("BZNick", "bznickcomands")
        emojies = self.db.get("BZNick", "bznickemoji")
        l = len(com)
        listComands = self.strings("count").format(l)
        if len(com) == 0:
            await utils.answer(message, self.strings("count").format(l))
            return
        for i in com:
            if i in emojies.keys():
                listComands += f"\n• <b><code>{i}</code> - {com[i]} |</b> {emojies[i]}"
            else:
                listComands += f"\n• <b><code>{i}</code> - {com[i]}</b>"
        await utils.answer(message, listComands)

    async def bznicknickcmd(self, message):
        """Use: .bznicknick (nick) to change nick to user or yourself. With -l argument will show all nicks."""
        args = utils.get_args_raw(message).strip()
        reply = await message.get_reply_message()
        nicks = self.db.get("BZNick", "bznicknicks")
        if args == "-l":
            str_nicks = "• " + "\n •".join(
                " --- ".join([f"<code>{user_id}</code>", f"<b>{nick}</b>"])
                for user_id, nick in nicks.items()
            )
            return await utils.answer(message, str_nicks)
        if not reply:
            user = await message.client.get_entity(message.sender_id)
        else:
            user = await message.client.get_entity(reply.sender_id)
        if not args:
            if str(user.id) in nicks:
                nicks.pop(str(user.id))
            self.db.set("BZNick", "bznicknicks", nicks)
            return await utils.answer(
                message,
                self.strings("nick-changed").format(user.id, user.first_name),
            )
        lst = []
        nick = ""
        nicks[str(user.id)] = args
        self.db.set("BZNick", "bznicknicks", nicks)
        await utils.answer(
            message,
            self.strings("nick-changed").format(user.id, args),
        )

    async def bznickbackcmd(self, message):
        """Backup BZNick commands.\n .bznickback to see arguments."""
        args = utils.get_args_raw(message).strip()
        comands = self.db.get("BZNick", "bznickcomands")
        emojies = self.db.get("BZNick", "bznickemoji")
        file_name = "BZNickBackUp.pickle"
        id = message.to_id
        reply = await message.get_reply_message()
        if not args:
            await utils.answer(
                message,
                self.strings("backup-args-help"),
            )
        if args == "-b":
            try:
                await message.delete()
                dict_all = {"bznick": comands, "emj": emojies}
                with open(file_name, "wb") as f:
                    pickle.dump(dict_all, f)
                await message.client.send_file(id, file_name)
            except Exception as e:
                await utils.answer(message, f"<b>Ошибка:\n</b>{e}")
        elif args == "-l" and reply:
            try:
                if not reply.document:
                    await utils.answer(message, self.strings("itsnotafile"))
                await reply.download_media(file_name)
                with open(file_name, "rb") as f:
                    data = pickle.load(f)
                bznick = data["bznick"]
                emj = data["emj"]
                result_bznick = dict(comands, **bznick)
                result_emj = dict(emojies, **emj)
                self.db.set("BZNick", "bznickcomands", result_bznick)
                self.db.set("BZNick", "bznickemoji", result_emj)
                await utils.answer(message, self.strings("actualised"))
            except Exception as e:
                await utils.answer(message, self.strings("error-with-type").format(e))

    async def bznickblockcmd(self, message):
        """Use: .bznickblock to add/remove exception (use in needed chat).\nUse: .bznickblock list to see exceptions.\nUse .bznickblock (id) to remove chat from exceptions."""
        args = utils.get_args_raw(message)
        ex = self.db.get("BZNick", "exlist")
        if not args:
            a = await message.client.get_entity(message.to_id)
            if a.id in ex:
                ex.remove(a.id)
                self.db.set("BZNick", "exlist", ex)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(
                    message,
                    self.strings("chat-included").format(name),
                )
            else:
                ex.append(a.id)
                self.db.set("BZNick", "exlist", ex)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(
                    message,
                    self.strings("chat-excluded").format(name),
                )
        elif args.isdigit():
            args = int(args)
            if args in ex:
                ex.remove(args)
                self.db.set("BZNick", "exlist", ex)
                a = await message.client.get_entity(args)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(
                    message,
                    self.strings("chat-excluded").format(name),
                )
            else:
                try:
                    a = await message.client.get_entity(args)
                except:
                    await utils.answer(message, self.strings("is-wrong"))
                ex.append(args)
                self.db.set("BZNick", "exlist", ex)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(message, self.strings("id-wrong"),
                )
        elif args == "list":
            ex_len = len(ex)
            if ex_len == 0:
                await utils.answer(message, self.strings("empty-exclude"))
                return
            sms = self.strings("excluded-chats")
            for i in ex:
                try:
                    a = await message.client.get_entity(i)
                except:
                    await utils.answer(message, self.strings("id-wrong"))
                    return
                try:
                    name = a.title
                except:
                    name = a.first_name
                sms += f"\n• <b><u>{name}</u> --- </b><code>{i}</code>"
            await utils.answer(message, sms)
        else:
            await utils.answer(message, self.strings("s-t-wrong"))

    async def useracceptbzcmd(self, message):
        """Adding/removing users/chats, allowed to use your commands.\n .useracceptbz {id/reply}\nTo add chat use without reply and args."""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        userA = self.db.get("BZNick", "useracceptbz")
        if not reply and not args and message.is_group:
            chat = message.chat
            if chat.id not in userA["chats"]:
                userA["chats"].append(chat.id)
                return await utils.answer(
                    message,
                    self.strings("on-in-chat").format(chat.title),
                )
            else:
                userA["chats"].remove(chat.id)
                return await utils.answer(
                    message,
                    self.strings("off-in-chat").format(chat.title),
                )
        elif args == "-l":
            sms = self.strings("who-have")
            for k, v in userA.items():
                if k == "chats":
                    sms += self.strings("chats-s")
                else:
                    sms += self.strings("users-s")
                for i in v:
                    try:
                        user = (
                            (await message.client.get_entity(int(i))).title
                            if k == "chats"
                            else (await message.client.get_entity(int(i))).first_name
                        )
                        sms += f"\n<b>• <u>{user}</u> ---</b> <code>{i}</code>"
                    except:
                        sms += f"\n<b>•</b> <code>{i}</code>"
            await utils.answer(message, sms)
        elif args or reply:
            args = int(args) if args.isdigit() else reply.sender_id
            if args in userA["users"]:
                userA["users"].remove(args)
                self.db.set("BZNick", "useracceptbz", userA)
                await utils.answer(
                    message,
                    self.strings("off-for-usr").format(args)
                )
            elif args in userA["chats"]:
                userA["chats"].remove(args)
                self.db.set("BZNick", "useracceptbz", userA)
                await utils.answer(
                    message, self.strings("off-in-chat").format(args)
                )
            elif (
                    args not in userA["chats"]
                    and type(await message.client.get_entity(args)) == Channel
            ):
                userA["chats"].append(args)
                self.db.set("BZNick", "useracceptbz", userA)
                await utils.answer(
                    message, self.strings("on-in-chat").format(args)
                )
            else:
                userA["users"].append(args)
                self.db.set("BZNick", "useracceptbz", userA)
                await utils.answer(
                    message,
                    self.strings("on-for-usr").format(args),
                )
        else:
            await utils.answer(message, self.strings("s-t-wrong"))

    async def bznickconfcmd(self, message):
        """Setting up the template for BZNick"""
        conf = self.db.get("BZNick", "bznickconfigurate", conf_default)
        args = utils.get_args_raw(message)
        if not args:
            sms = self.strings("config1")
            s1 = "\n".join(
                [
                    " | ".join([key, value[1], "✅" if value[0] else "❌"])
                    for key, value in conf["-s1"].items()
                ]
            )
            s2 = "\n".join(
                [
                    " | ".join([key, value[1], "✅" if value[0] else "❌"])
                    for key, value in conf["-s2"].items()
                ]
            )
            s3 = "\n".join(
                [
                    " | ".join([key, value[1], "✅" if value[0] else "❌"])
                    for key, value in conf["-s3"].items()
                ]
            )
            sE = "\n".join(
                [
                    " | ".join([key, value[1], "✅" if value[0] else "❌"])
                    for key, value in conf["-sE"].items()
                ]
            )
            sS = "\n".join(
                [
                    " | ".join([key, value[1], "✅" if value[0] else "❌"])
                    for key, value in conf["-sS"].items()
                ]
            )
            msg_text = self.strings("config2").format(s1, s2, s3, sE, sS)
            return await utils.answer(message, msg_text)
        args = args.split(" ")
        if len(args) <= 1:
            return await utils.answer(message, self.strings("less-then-2"))
        try:
            if args[0] == "-s1" or args[0] == "-s2" or args[0] == "-s3":
                if conf[args[0]][args[1]][0]:
                    conf[args[0]][args[1]][0] = False
                else:
                    conf[args[0]][args[1]][0] = True
            elif args[0] == "-sE" or args[0] == "-sS":
                for i in conf[args[0]].keys():
                    conf[args[0]][i][0] = False
                conf[args[0]][args[1]][0] = True
            else:
                return await utils.answer(message, self.strings("arg-unknown"))
        except:
            return await utils.answer(message, self.strings("num-unknown"))
        self.db.set("BZNick", "bznickconfigurate", conf)
        await utils.answer(message, self.strings("done"))

    async def mmminfocbzmd(self, message):
        """Read mod information and updates."""
        await utils.answer(message, self.strings("whatschanged"))
    async def watcher(self, message):
        try:
            status = self.db.get("BZNick", "status")
            comand = self.db.get("BZNick", "bznickcomands")
            rezjim = self.db.get("BZNick", "bznickrezjim")
            emojies = self.db.get("BZNick", "bznickemoji")
            ex = self.db.get("BZNick", "exlist")
            nicks = self.db.get("BZNick", "bznicknicks")
            users_accept = self.db.get("BZNick", "useracceptbz")
            conf = self.db.get("BZNick", "bznickconfigurate", conf_default)

            chat_bznick = await message.client.get_entity(message.to_id)
            if status != 1 or chat_bznick.id in ex:
                return
            me_id = (await message.client.get_me()).id

            if (
                message.sender_id not in users_accept["users"]
                and message.sender_id != me_id
                and chat_bznick.id not in users_accept["chats"]
            ):
                return
            me = await message.client.get_entity(message.sender_id)

            if str(me.id) in nicks.keys():
                nick = nicks[str(me.id)]
            else:
                nick = me.first_name
            if ' ' in message.text and '\n' not in message.text:
                args = message.text.split(' ', 1)[0].casefold()+' '+message.text.split(' ', 1)[1]
            elif '\n' in message.text:
                arl = message.text.split('\n', 1)
                if ' ' in arl[0]:
                    args = arl[0].split(' ', 1)[0].casefold() + ' ' + arl[0].split(' ', 1)[1] + '\n' + arl[1]
                else:
                    args = arl[0].casefold()+'\n'+arl[1]
            else:
                args = message.text.casefold()
            lines = args.splitlines()
            tags = lines[0].split(" ")
            if not tags[-1].startswith("@"):
                reply = await message.get_reply_message()
                user = await message.client.get_entity(reply.sender_id)
            else:
                if not tags[-1][1:].isdigit():
                    user = await message.client.get_entity(tags[-1])
                else:
                    user = await message.client.get_entity(int(tags[-1][1:]))
                lines[0] = lines[0].rsplit(" ", 1)[0]
            detail = lines[0].split(" ", maxsplit=1)
            if len(detail) < 2:
                detail.append(" ")
            if detail[0] not in comand.keys():
                return
            detail[1] = " " + detail[1]
            user.first_name = (
                nicks[str(user.id)] if str(user.id) in nicks else user.first_name
            )
            sE = "".join(
                [
                    "".join([value[1] if value[0] else ""])
                    for key, value in conf["-sE"].items()
                ]
            )
            s1 = [
                "".join(
                    [value[2] if value[0] else "" for value in conf["-s1"].values()]
                ),
                "".join(
                    [
                        value[3] if value[0] else ""
                        for value in dict(reversed(list(conf["-s1"].items()))).values()
                    ]
                ),
            ]
            s2 = [
                "".join(
                    [value[2] if value[0] else "" for key, value in conf["-s2"].items()]
                ),
                "".join(
                    [
                        value[3] if value[0] else ""
                        for value in dict(reversed(list(conf["-s2"].items()))).values()
                    ]
                ),
            ]
            s3 = [
                "".join(
                    [value[2] if value[0] else "" for key, value in conf["-s3"].items()]
                ),
                "".join(
                    [
                        value[3] if value[0] else ""
                        for value in dict(reversed(list(conf["-s3"].items()))).values()
                    ]
                ),
            ]
            sS = "".join(
                [
                    "".join([value[2] if value[0] else ""])
                    for key, value in conf["-sS"].items()
                ]
            )

            bznickMessageSend = ""
            if detail[0] in emojies.keys():
                bznickMessageSend += emojies[detail[0]] + " | "
            bznickMessageSend += f"<a href=tg://user?id={me.id}>{nick}</a> {s1[0]}{comand[detail[0]]}{s1[1]} <a href=tg://user?id={user.id}>{user.first_name}</a>{detail[1]}"
            if len(lines) >= 2:
                bznickMessageSend += "\n{0} {1[0]}{2}{1[1]} {3[0]}{4}{3[1]}".format(
                    sE, s2, self.strings("with-replica"), s3, sS.join(lines[1:])
                )
            if rezjim == 1:
                return await utils.answer(message, bznickMessageSend)
            else:
                return await message.respond(bznickMessageSend)
        except:
            pass

    def merge_dict(self, d1, d2):
        d_all = {**d1, **d2}
        for key in d_all:
            d_all[key] = {**d1[key], **d_all[key]}
        return d_all
