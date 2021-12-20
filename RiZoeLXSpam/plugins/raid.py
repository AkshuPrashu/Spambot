
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
from resources.data import RAID, REPLYRAID, RiZoeLX

que = {}

@Riz.on(events.NewMessage(pattern=r"\.fuk"))
@Riz2.on(events.NewMessage(pattern=r"\.fuk"))
@Riz3.on(events.NewMessage(pattern=r"\.fuk"))
@Riz4.on(events.NewMessage(pattern=r"\.fuk"))
@Riz5.on(events.NewMessage(pattern=r"\.fuk"))
@Riz6.on(events.NewMessage(pattern=r"\.fuk"))
@Riz7.on(events.NewMessage(pattern=r"\.fuk"))
@Riz8.on(events.NewMessage(pattern=r"\.fuk"))
@Riz9.on(events.NewMessage(pattern=r"\.fuk"))
@Riz10.on(events.NewMessage(pattern=r"\.fuk"))
@Riz11.on(events.NewMessage(pattern=r"\.fuk"))
@Riz12.on(events.NewMessage(pattern=r"\.fuk"))
@Riz13.on(events.NewMessage(pattern=r"\.fuk"))
@Riz14.on(events.NewMessage(pattern=r"\.fuk"))
@Riz15.on(events.NewMessage(pattern=r"\.fuk"))
@Riz16.on(events.NewMessage(pattern=r"\.fuk"))
@Riz17.on(events.NewMessage(pattern=r"\.fuk"))
@Riz18.on(events.NewMessage(pattern=r"\.fuk"))
@Riz19.on(events.NewMessage(pattern=r"\.fuk"))
@Riz20.on(events.NewMessage(pattern=r"\.fuk"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(RiZoeL) == 2:
            user = str(RiZoeL[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on Team MLO's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(RiZoeL[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on Team MLO's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(RiZoeL[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@Riz.on(events.NewMessage(incoming=True))
@Riz2.on(events.NewMessage(incoming=True))
@Riz3.on(events.NewMessage(incoming=True))
@Riz4.on(events.NewMessage(incoming=True))
@Riz5.on(events.NewMessage(incoming=True))
@Riz6.on(events.NewMessage(incoming=True))
@Riz7.on(events.NewMessage(incoming=True))
@Riz8.on(events.NewMessage(incoming=True))
@Riz9.on(events.NewMessage(incoming=True))
@Riz10.on(events.NewMessage(incoming=True))
@Riz11.on(events.NewMessage(incoming=True))
@Riz12.on(events.NewMessage(incoming=True))
@Riz13.on(events.NewMessage(incoming=True))
@Riz14.on(events.NewMessage(incoming=True))
@Riz15.on(events.NewMessage(incoming=True))
@Riz16.on(events.NewMessage(incoming=True))
@Riz17.on(events.NewMessage(incoming=True))
@Riz18.on(events.NewMessage(incoming=True))
@Riz19.on(events.NewMessage(incoming=True))
@Riz20.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@Riz.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz2.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz3.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz4.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz5.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz6.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz7.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz8.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz9.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz10.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz11.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz12.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz13.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz14.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz15.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz16.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz17.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz18.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz19.on(events.NewMessage(pattern=r"\.hardcore"))
@Riz20.on(events.NewMessage(pattern=r"\.hardcore"))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Rizx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(RiZoeL[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in RiZoeLX:
                text = f" can't raid on Team MLO's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in RiZoeLX:
                text = f" can't raid on Team MLO's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Riz.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz2.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz3.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz4.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz5.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz6.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz7.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz8.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz9.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz10.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz11.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz12.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz13.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz14.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz15.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz16.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz17.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz18.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz19.on(events.NewMessage(pattern=r"\.dhardcore"))
@Riz20.on(events.NewMessage(pattern=r"\.dhardcore"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
