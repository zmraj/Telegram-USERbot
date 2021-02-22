from . import *


@asst_cmd("ban")
async def banhammer(event):
    x = await event.get_reply_message()
    if x is None:
        return await event.edit("Please reply to someone to ban him.")
    if x.fwd_from:
        target = x.fwd_from.from_id.user_id
        if not is_blacklisted(target):
            blacklist_user(target)
            await asst.send_message(event.chat_id, f"#BAN\nUser - {target}")
            await asst.send_message(
                target,
                "`GoodBye! You have been banned.`\n**Further messages you send will not be forwarded.**",
            )
        else:
            await asst.send_message(event.chat_id, f"User is already banned!")
    return


@asst_cmd("unban")
async def banhammer(event):
    x = await event.get_reply_message()
    if x is None:
        return await event.edit("Please reply to someone to ban him.")
    if x.fwd_from:
        target = x.fwd_from.from_id.user_id
        if is_blacklisted(target):
            rem_blacklist(target)
            await asst.send_message(event.chat_id, f"#UNBAN\nUser - {target}")
            await asst.send_message(target, "`Congrats! You have been unbanned.`")
        else:
            await asst.send_message(event.chat_id, f"User was never banned!")
    return
