from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/0a8cec1011596c33154d8.jpg"
  

          
rizoel = "๐ง๐๐๐  ๐ ๐๐ข ๐๐๐ฅ๐.\n\n"

rizoel += f"โโโโโโโโโโโโโโโโโโโ\n"

rizoel += f" **แดสแดสแดษด แด แดสsษชแดษด** : `3.9.6`\n"

rizoel += f" **แดแดสแดแดสแดษด แด แดสsษชแดษด** : `{version.__version__}`\n"

rizoel += f" **Bot แด แดสsษชแดษด**  : `{rizoelversion}`\n"

rizoel += f"โโโโโโโโโโโโโโโโโโโ\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".robot"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("แดแดกษดแดส", "https://t.me/TG_GoDfaTHeR")
        ]
        ]
        )
    
