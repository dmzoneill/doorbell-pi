import telegram
import secrets

class RingSignaler:

    def __init__(self, tokenHandler):
        self.tokenHandler = tokenHandler

    def getTokenAsString(self):
        return self.tokenHandler.generateToken().decode("utf-8")
    
    def composeMessage(self):
        host = "http://raspberrypi:9000/"
        messageText = "Ring! Ring! Open: "
        
        token = self.getTokenAsString()
        url = host + token

        message = messageText + url
        return message

    def sendNotification(self):
        bot = telegram.Bot(token=secrets.telegramToken)

        message = self.composeMessage()
        bot.sendMessage(secrets.chatId, message)