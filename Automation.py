################################################################################
################################################################################
####################### NÃO ALTERAR DESTA LINHA PRA BAIXO ######################
################################################################################
################################################################################

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from datetime import datetime
import time
import re
import requests
import json

class Bot:

    driver = None
    LOGIN_SUCCESS = None
    
    ACCOUNT_BALANCE = None
    BASE_URL = ""
    switchGale = None
    count = 1
    
    # Inicia | Inicializar a biblioteca Selenium, abre o browser e carrega a renderiza a página web.
    def Start(self):

        print("")
        print("")
        print("##########################################")  
        print("# Inicializando Bot - Hora da forra !!!  #")
        print("##########################################")
      
        global BASE_URL
        BASE_URL = 'https://blaze1.space/en/games/crash'
            
        global driver
        
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1300,1000")
        chrome_options.add_experimental_option("detach", True)
        
        chrome_options.add_argument("--log-level=3")
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_position(500, 0, windowHandle="current")
        driver.get(BASE_URL)

        print("")
        print("#############################################")
        print("# Efetuando o login na plataforma Blaze...  #")

    # Fecha | Fecha todas as instancias e processos realizacionados a biblioteca Selenium
    def Stop(self):
        
        print("")
        print("######################")
        print("# Finalizando Bot... #")
        driver.quit()
        print("# Bot finalizado !!! #")
        print("######################")
        print("")
        print("")
    
    # Login
    def Login(self, email, password):
        
        error = None
        global LOGIN_SUCCESS
        
        try:
            wait = WebDriverWait(driver, 10)
            LOGIN_BUTTON = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div[2]/div/div/div[1]/a')))
            LOGIN_BUTTON.click()
            
            time.sleep(1)
            EMAIL_INPUT = driver.find_elements(By.CLASS_NAME, 'input-wrapper')[0].find_element(By.TAG_NAME, 'input')
            EMAIL_INPUT.send_keys(email)
            
            PASSWORD_INPUT = driver.find_elements(By.CLASS_NAME, 'input-wrapper')[1].find_element(By.TAG_NAME, 'input')
            PASSWORD_INPUT.send_keys(password)
            
            SUBMIT_BUTTON = driver.find_element(By.CLASS_NAME, 'submit')
            SUBMIT_BUTTON.click()
            
            LOGIN_SUCCESS = True
            
        except Exception as e:
            error = [False, e]
        finally:
            if error:
                print("Error", error)
                LOGIN_SUCCESS = False
                return error
            else:
                print("# Login realizado com sucesso !!!           #")
                print("#############################################")
                print("")
                print("")
                print("##################################################################")
                print("# Partida em andamento, aguardando o inicio da proxima rodada... #")
                print("##################################################################")
                print("")
                return [LOGIN_SUCCESS, None]
            
    ############### Saldo da conta ###############
    def Get_Balance(self):
        
        time.sleep(0.5)
        balanceValue = driver.find_elements(By.CSS_SELECTOR, '.wallet-dropdown')

        for e in balanceValue:
            teste = e.text.replace(" ", "")
            teste2 = teste.replace("R$", "")
            return teste2
    
    def BetCrash(self, bets, return_results, numberCrashs, valueCrash):

        # Variavel
        valueAmout = ""

        # Switch de verificação se atende ou não aos criterios para apresentação das mensagens.
        switch = False

        # Coleta a data e hora no momento da entrada da aposta
        dataTime = datetime.now()

        #Contador do gale
        y = 0
        # total_bet = 0
  
        ############### Verifica se há apenas uma aposta ###############
        # if len(bets) > 1:
        #     print("O campo so pode receber um objeto.")
        #     return False
        
        # ############### Verifica se a formatação da aposta esta correta e se há saldo suficiente ###############
        # for bet in bets:
        #     if len(bet) < 2:
        #         print("Formato incorreto", "tamanho")
        #         return False
            
        #     if bet['amount'] * 1 > 0:
        #         total_bet += bet['amount']
        #     else:
        #         print("Formato incorreto", "quantidade incorreta")
        #         return False

        ############### Aguarda o início da proxima aposta ###############
        current_status = None
        while current_status != "waiting":
            current_status = requests.get('https://blaze.com/api/crash_games/current')
            if current_status.status_code == 200:
                current_status = current_status.json()['status']
            print(current_status)
            # time.sleep(1)
            #time.sleep(0.1)
        
        ############### Pega a referencia dos campos e botoes para entrada ###############
        INPUT_AMOUNT = driver.find_element(By.XPATH, '//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input')
        INPUT_AUTO_REMOVE = driver.find_element(By.XPATH, '//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[2]/div[1]/input')
        BET_BUTTON = driver.find_element(By.XPATH, '//*[@id="crash-controller"]/div[1]/div[2]/div[2]/button')
        
        ############### Realiza a aposta###############
        for bet in bets:
            elements = driver.find_elements(By.CSS_SELECTOR, '#crash-recent')
            for e in elements:
                x = re.split('\n', e.text.replace("X",""))
                x.remove("PREVIOUS")
                for i in range(numberCrashs):
                    # Verifica se o valor multiplicador é igual a 1.000.00
                    if len(x[i]) >= 8:
                        a = x[i].replace(".", "")
                        b = float(a.replace(",", "."))
                        crashValue = b
                    else:
                        crashValue = float(x[i].replace(",", "."))

                    # Contador para validação dos criterios do gale
                    if crashValue <= valueCrash:
                        y += 1
                    else:
                        print("")
                        print("###################################################")
                        print("#    Aguardando o inicio da proxima rodada ...    #")
                        print("###################################################")
                        print("")
                        print("###################################################")
                        print("#            Ultima sequencia de crashs           #")
                        print("###################################################")
                        print("")
                        print(x)
                        print("")
                        print("###################################################") 
                        print("")
                        print(" >>> Nao atende a todos os criterios de entrada <<<")
                        print(" >>>         Aguardando a proxima rodada        <<<")
                        print("")
                        print("###################################################")
                        print("")
                        switch = False
                        break

            if y == numberCrashs:
                print("")
                print("###################################################")
                print("#    Aguardando o inicio da proxima rodada ...    #")
                print("###################################################")
                print("")
                print("###################################################")
                print("#            Ultima sequencia de crashs           #")
                print("###################################################")
                print("")               
                print(x)
                print("")
                print("###################################################") 
                print("")
                print(" <<<   Atende a todos os criterios de entrada   >>>")
                print(" <<<        Aguardando a proxima rodada         >>>")
                print("")
                print("###################################################")
                print("")
                switch = True
                print(">>> Data e hora da entrada:", dataTime.strftime('%d/%m/%Y %H:%M'))
                print("")
                print(">>> Saldo da conta R$:", self.Get_Balance())

                # Verifica se esta em gale
                if self.switchGale == True:
                    for i in range(6):
                        INPUT_AMOUNT.send_keys(Keys.BACKSPACE)
                        i += 1
                    valueAmout = str("%.2f" % (bet['amount'] * self.count))
                    INPUT_AMOUNT.send_keys(valueAmout)
                    print("\n>>> Valor da aposta R$: " + valueAmout)
                else:
                    for i in range(6):
                        INPUT_AMOUNT.send_keys(Keys.BACKSPACE)
                        i += 1
                    valueAmout = str("%.2f" % (bet['amount']))
                    INPUT_AMOUNT.send_keys(valueAmout)
                    print("\n>>> Valor da aposta R$: " + valueAmout)
                
                # Limpo os campos Amount e Cashout At
                # time.sleep(0.1)
                
                if bet['autoCashout'] > 1.00:
                    for i in range(4):
                        INPUT_AUTO_REMOVE.send_keys(Keys.BACKSPACE)
                        i += 1
                    INPUT_AUTO_REMOVE.send_keys(str(bet['autoCashout']))
                else:
                    for i in range(4):
                        INPUT_AUTO_REMOVE.send_keys(Keys.BACKSPACE)
                        i += 1
                    INPUT_AUTO_REMOVE.send_keys('1.01')
                
                # time.sleep(0.1)

                # Evento click do botão de apostas
                print("\n>>> Sair em: " + "%.2f" % bet['autoCashout'] + "X")
                #BET_BUTTON.click()
                print("CLIQUE BOTÃO")

            if return_results == True:
            
                current_result = None
                current_status = None
                while current_status != "complete":
                    result = requests.get('https://blaze.com/api/crash_games/current')
                    if result.status_code == 200:
                        current_status = result.json()['status']
                        current_result = result.json()
                    #time.sleep(1)
                
                result_crash = float(current_result['crash_point'])
                
                bet_results = []
                total_result = 0
                
                for bet in bets:
                    result = None
                    if self.switchGale == True:
                        if bet['autoCashout'] <= result_crash:
                            result = bet['autoCashout'] * float(valueAmout)
                        else:
                            result = 0 - float(valueAmout)  
                    else:
                        if bet['autoCashout'] <= result_crash:
                            result = bet['autoCashout'] * bet['amount']
                        else:
                            result = 0 - bet['amount']    
                                
                    total_result += result
                    bet_results.append({ "autoCashout": bet['autoCashout'], "amount": result})   

                if switch == True:
                    if total_result > 0.00:
                        print("\n>>> Multiplicador no momento do Crash:", "%.2f" % result_crash + "X")
                        print("\n>>> Ganho (Valor da aposta + Lucro) R$", "%.2f" % total_result)
                        print("")
                        self.count = 1
                        self.switchGale = False
                    else:
                        print("\n>>> Multiplicador no momento do Crash:", "%.2f" % result_crash + "X")
                        print("\n>>> Perda R$", "%.2f" % total_result)
                        print("")
                        self.switchGale = True
                        self.count *=2