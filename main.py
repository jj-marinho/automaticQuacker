import os
import telegram
from telegram import ParseMode

def webhook(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=create_quack(update.message.text), parse_mode=ParseMode.MARKDOWN)
    return "ok"

def create_quack(text):
	msg = "```\n"

	# Top textbox border
	msg += "    ----------------------------    \n"

	# Creates a textbox with 18 chars per line,
	# Plus 4 chars padding and "<>" border
	for i in range(len(text)):
		## Padding at the start of every line and "<" border delimiter 
		if i % 18 == 0:
			msg += "   <     {}".format(text[i])

		# When the end of line is reached, create some padding and a ">" border
		elif i % 18 == 17 and i != 1:
			msg += "{}     >    ".format(text[i])
			if i != len(text) - 1:
				msg += "\n"
		
		# Adds each character of the current line
		else:
			msg += text[i]

		# Adds final padding and border ">"
		# Needed because sometimes the text doesn't reach the 18 chars
		if i == len(text) - 1 and len(text) % 18:
			for j in range(18 - i % 18):
				msg += " "
			msg += "    >"

	# Adding bottom border on the screen	
	msg += "\n    ----------------------------    \n"

	# Adds a very cool duck
	msg += """                     ^
              ..    /
             ( '`< /
              )(
       ( ----'  '.
       (         ;
        (_______,' 
jgs~^~^~^~^~^~^~^~^~^~^~\n```"""

	return msg
