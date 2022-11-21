from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

with open('dados.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)

train = []

for row in data:
    train.append(row['questao'])
    train.append(row['resposta'])

chatbot = ChatBot('Helpy',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.BestMatch'
                  ])
chatbot.storage.drop()

trainer = ListTrainer(chatbot)

trainer.train(train)

while True:
    questao = input('\nYou: ')
    resposta = chatbot.get_response(questao)
    
    if float(resposta.confidence) > 0.5:
        resposta = str(resposta).replace(';', '\n')
        print(f'Bot: {resposta}')
    else:
        print("Eu não entendi :(")