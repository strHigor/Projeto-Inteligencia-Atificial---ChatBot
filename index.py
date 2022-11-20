# Integrantes: Higor Barbosa, Fillipe Cabral, Mateus Basilio
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import utils as utils

bot = ChatBot('Irineu')
bot = ChatBot(
    'Irineu',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
    
conversa = ListTrainer(bot)
conversa.train([
    'if',
    'else',
    'elif',
    'condicional',
])

while True:
    try:
        resposta = input("Usuário: ")
        if resposta == "":
            print("Irineu: Digite algo.")

        else:
            response = bot.get_response(resposta)
            while response.confidence == 0:
                response = bot.get_response(resposta)

            if float(response.confidence) > 0.5:
                print(utils.tratar_resposta(response))
                #print("Irineu: ", response)
            else:
                print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break