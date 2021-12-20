from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/0a8cec1011596c33154d8.jpg"
  

          
rizoel = "𝗧𝗘𝗔𝗠 𝗠𝗟𝗢 𝗛𝗘𝗥𝗘.\n\n"

rizoel += f"━━━━━━━━━━━━━━━━━━━\n"

rizoel += f" **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f" **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f" **Bot ᴠᴇʀsɪᴏɴ**  : `{ProfessorVersion}`\n"

rizoel += f"━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴏᴡɴᴇʀ", "https://t.me/TG_GoDfaTHeR")
        ]
        ]
        )
    
