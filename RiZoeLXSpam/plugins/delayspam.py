async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS



@Riz.on(events.NewMessage(pattern=r"\.dspam"))
@Riz2.on(events.NewMessage(pattern=r"\.dspam"))
@Riz3.on(events.NewMessage(pattern=r"\.dspam"))
@Riz4.on(events.NewMessage(pattern=r"\.dspam"))
@Riz5.on(events.NewMessage(pattern=r"\.dspam"))
@Riz6.on(events.NewMessage(pattern=r"\.dspam"))
@Riz7.on(events.NewMessage(pattern=r"\.dspam"))
@Riz8.on(events.NewMessage(pattern=r"\.dspam"))
@Riz9.on(events.NewMessage(pattern=r"\.dspam"))
@Riz10.on(events.NewMessage(pattern=r"\.dspam"))
@Riz11.on(events.NewMessage(pattern=r"\.dspam"))
@Riz12.on(events.NewMessage(pattern=r"\.dspam"))
@Riz13.on(events.NewMessage(pattern=r"\.dspam"))
@Riz14.on(events.NewMessage(pattern=r"\.dspam"))
@Riz15.on(events.NewMessage(pattern=r"\.dspam"))
@Riz16.on(events.NewMessage(pattern=r"\.dspam"))
@Riz17.on(events.NewMessage(pattern=r"\.dspam"))
@Riz18.on(events.NewMessage(pattern=r"\.dspam"))
@Riz19.on(events.NewMessage(pattern=r"\.dspam"))
@Riz20.on(events.NewMessage(pattern=r"\.dspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Rizoelsexy = Rizoel[1:]
        if len(Rizoelsexy) == 2:
            message = str(Rizoelsexy[1])
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
