from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/0a8cec1011596c33154d8.jpg"

Riz_Help = "π₯ π§πππ  π ππ’ π₯\n\n"
 
Riz_Help += f"__α΄α΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ ΚΙͺα΄’α΄α΄Κ x sα΄α΄α΄__\n\n"

Riz_Help += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

Riz_Help += f" `.bot` - to check ping\n `.robot` - to check bot alive/version (only main userbot will reply)\n .`reboot` - to restart all spam bots\n\n"
 
Riz_Help += f" β§ π»π΄π°ππ΄ π²πΌπ³ β§\n\n"

Riz_Help += f" `.bleave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

Riz_Help += f" `.fuk` - to raid\n `.hardcore` - to active reply raid\n `.dhardcore` - to de-active reply raid\n `.bspam` - this cmd use for Normal spam\n `.bigbspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.dspam` - this cmd use for delay spam\n\n"


@Riz.on(events.NewMessage(pattern=".bhelp"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("α΄α΄‘Ι΄α΄Κ", "https://t.me/TG_GoDfaTHeR")
        ]
        ]
        )                                                         
