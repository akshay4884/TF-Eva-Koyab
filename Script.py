class script(object):
    START_TXT ="""𝐇𝐄𝐋𝐋𝐎 {},
𝐌𝐘 𝐍𝐀𝐌𝐄 𝐈𝐒 <a href=https://t.me/{}>{}</a>,𝐈 𝐂𝐀𝐍 𝐏𝐑𝐎𝐕𝐈𝐃𝐄 𝐌𝐎𝐕𝐈𝐄𝐒 𝐀𝐍𝐃 𝐒𝐄𝐑𝐈𝐄𝐒, 𝐈 𝐖𝐎𝐑𝐊 𝐅𝐎𝐑 𝐓𝐄𝐀𝐌 𝐌𝐄𝐆𝐀𝐓𝐑𝐎𝐍𝐙 𝐌𝐎𝐕𝐈𝐄𝐙😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>🥱 My Name : {}
🕵‍♂ Developer : <a href='https://t.me/dark_lord_8'>★ 𝘼𝙆𝙎𝙃𝘼𝙔 ★</a>
📚 Library : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
🖥 Language : പച്ച മലയാളം
🎪 Data Base : ᴋᴏʟʟᴀᴍ
🔋 Bot Group : <a href='https://t.me/+AdnOzGkxSo84NzVl'>𝙏𝙀𝙇𝙀𝙁𝙇𝙄𝙓</a></b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖶𝖺𝗌 𝖬𝖺𝗄𝖾𝖽 𝖳𝖺𝗄𝗂𝗇𝗀 𝖲𝗈𝗆𝖺𝗇𝗒 𝖱𝖾𝗉𝗈𝗌 𝖮𝖿 𝖮𝗍𝗁𝖾𝗋 𝖪𝗂𝗇𝖽 𝖡𝗈𝗍𝗌
𝖲𝖮𝖴𝖱𝖢𝖤 𝖢𝖮𝖣𝖤 ~ 𝖭𝖮𝖳 𝖠𝖵𝖠𝖨𝖫𝖠𝖡𝖫𝖤 𝖱𝖨𝖦𝖧𝖳 𝖭𝖮𝖶</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/M4MHD)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
