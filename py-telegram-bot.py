import telebot

CHAVE_API = "Sua chave do telegram aqui"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["hd"])
def hd(mensagem):
    bot.send_message(mensagem.chat.id, "Deixe o tamanho do hd que você deseja, e deixe o seu endereço logo você será atendido por um de nossos atendentes a Neltech agradece pela preferencia: Tempo de espera em 20min")

@bot.message_handler(commands=["memoria"])
def memoria(mensagem):
    bot.send_message(mensagem.chat.id, "Deixe o tamanho da Memoria que você deseja, e deixe o seu endereço logo você será atendido por um de nossos atendentes a Neltech agradece pela preferencia: Tempo de espera em 20min")

@bot.message_handler(commands=["tela"])
def tela(mensagem):
    bot.send_message(mensagem.chat.id, "Deixe o modelo e tamanho da tela e tambem deixe o seu endereço logo você será atendido por um de nossos atendentes a Neltech agradece pela preferencia: Tempo de espera em 20min")

@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "É brincadeira não temos salada não hahaha , clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /hd Hd
    /memoria Memoria
    /tela Tela
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@Neltech.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Emanuel proprietario da Neltech mandou um abraço de volta")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Reclamar de um pedido
     /opcao3 Mandar um abraço pro Emanuel
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()