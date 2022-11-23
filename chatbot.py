from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

def obter_resposta(intencao):
    with open('resposta.json', 'r', encoding='utf-8') as resposta:
        dados_resposta = json.load(resposta)

        for i in dados_resposta:
            if i['intencao'] == intencao:
                return(str(i['resposta']).replace(";", "\n"))

with open('intencao.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)

train = []

for row in data:
    train.append(row['pergunta'])
    train.append(row['intencao'])

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
        resposta = obter_resposta(str(resposta))
        return f'{resposta}\n\nHelpy: Qual a próxima dúvida?'
         
    else:
        return 'Eu não entendi, tente novamente por favor.'