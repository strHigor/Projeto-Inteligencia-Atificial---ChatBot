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

def perguntar(mensagem):
    resposta = chatbot.get_response(mensagem)
    
    if float(resposta.confidence) > 0.5:
        resposta = str(resposta).replace(";", "\n")
        return f'{resposta}\n\nHelpy: Qual a próxima dúvida?'
         
    else:
        return 'Eu não entendi, tente novamente por favor.'