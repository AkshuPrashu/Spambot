import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS


@Riz.on(events.NewMessage(pattern=r"\.uspam"))
@Riz2.on(events.NewMessage(pattern=r"\.uspam"))
@Riz3.on(events.NewMessage(pattern=r"\.uspam"))
@Riz4.on(events.NewMessage(pattern=r"\.uspam"))
@Riz5.on(events.NewMessage(pattern=r"\.uspam"))
@Riz6.on(events.NewMessage(pattern=r"\.uspam"))
@Riz7.on(events.NewMessage(pattern=r"\.uspam"))
@Riz8.on(events.NewMessage(pattern=r"\.uspam"))
@Riz9.on(events.NewMessage(pattern=r"\.uspam"))
@Riz10.on(events.NewMessage(pattern=r"\.uspam"))
@Riz11.on(events.NewMessage(pattern=r"\.uspam"))
@Riz12.on(events.NewMessage(pattern=r"\.uspam"))
@Riz13.on(events.NewMessage(pattern=r"\.uspam"))
@Riz14.on(events.NewMessage(pattern=r"\.uspam"))
@Riz15.on(events.NewMessage(pattern=r"\.uspam"))
@Riz16.on(events.NewMessage(pattern=r"\.uspam"))
@Riz17.on(events.NewMessage(pattern=r"\.uspam"))
@Riz18.on(events.NewMessage(pattern=r"\.uspam"))
@Riz19.on(events.NewMessage(pattern=r"\.uspam"))
@Riz20.on(events.NewMessage(pattern=r"\.uspam"))
async def unlimitedspam(event):
  if event.sender_id in SUDO_USERS:
    try:
      op = event.text[7:]
      x = None
      while x == None:
        await event.client.send_message(event.chat, op)
        await asyncio.sleep(0.3)
    except Exception as e:
      await event.reply("Oops!! Something went wrong, Report In @Mlo_Empire\n\n" + str(e))
