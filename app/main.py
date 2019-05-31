from app.bot.bot import XtensibleBot
import os
import json

if __name__ == '__main__':
    token = ''
    with open(os.path.join('app/resources/auth.json')) as authfile:
        token = json.load(authfile)['token']
    xtensible_bot = XtensibleBot(token)
    xtensible_bot.run()
