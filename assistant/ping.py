# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from time import time


@asst_cmd("ping")
@owner
async def _(event):
    start = time()
    ms = (time() - start)
    await asst.send_message(
        event.chat_id,
        f"**Pong!!**\n `{ms}ms`",
    )
    return
