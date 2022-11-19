#Integrantes: Higor Barbosa, Fillipe Cabral, Mateus Basilio
from chatterbot.trainers import ListTrainer 
from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot import ChatBot 

bot = ChatBot('Pegasus')
conversa = ChatterBotCorpusTrainer(bot)
conversa = ListTrainer(bot)

conversa.train([
     'Quem é você?', 'Eu sou'
])

print("####Início da interação do Chatbot####")
while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print("Pégasus: ", resposta)
    else:
        print('Pégasus: Ainda não sei responder esta pergunta.')