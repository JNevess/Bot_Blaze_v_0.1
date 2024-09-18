from Automation import Bot

# Instancia o objeto da classe Bot
bot = Bot()

# Inicia o bot
bot.Start()

####################### NÃO ALTERAR DESTA LINHA PRA CIMA ####################### 





################################################################################
#####################      INFORMAÇÕES DE LOGIN       ##########################

# Digite entre as aspas o seu e-mail de acesso a Blaze
email = ""

# Digite entre as aspas o seu e-mail de acesso a Blaze
password = "" # Digite entre as aspas o seu e-mail de acesso a Blaze

################################################################################



################## PARAMETROS DE FUNCIONAMENTO DO BOT ##########################

# Valor para fechamento da aposta.
autoCashOut = 2.00

# Valor da aposta.
amount = 0.20

# Define a quantidade de crashs o bot aguarda para fazer a aposta.
numberCrashs = 1

# Define qual o valor limite para entrada do crash.
valueCrash = 1.99

################################################################################






####################### NÃO ALTERAR DESTA LINHA PRA BAIXO ######################

login, reason = bot.Login(email=email, password=password)

if login == True:

    #### CRASH ####
    while True:
        # bot.Get_Balance()
        crashBet = bot.BetCrash(bets=[{"autoCashout": autoCashOut, "amount": amount}], return_results=True, numberCrashs=numberCrashs, valueCrash=valueCrash)